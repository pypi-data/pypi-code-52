from clvm import KEYWORD_TO_ATOM

from clvm_tools import binutils
from clvm_tools.NodePath import LEFT, RIGHT, TOP

from .helpers import eval


CONS_KW = KEYWORD_TO_ATOM["c"]
QUOTE_KW = KEYWORD_TO_ATOM["q"]

MAIN_NAME = b""


def build_tree(items):
    """
    This function takes a Python list of items and turns it into a binary tree
    of the items, suitable for casting to an s-expression.
    """
    size = len(items)
    if size == 0:
        return []
    if size == 1:
        return items[0]
    half_size = size >> 1
    left = build_tree(items[:half_size])
    right = build_tree(items[half_size:])
    return (left, right)


def build_tree_program(items):
    """
    This function takes a Python list of items and turns it into a program that
    builds a binary tree of the items, suitable for casting to an s-expression.
    """
    size = len(items)
    if size == 0:
        return [QUOTE_KW, []]
    if size == 1:
        return items[0]
    half_size = size >> 1
    left = build_tree_program(items[:half_size])
    right = build_tree_program(items[half_size:])
    return [CONS_KW, left, right]


def flatten(sexp):
    """
    Return a (python) list of every atom.
    """
    if sexp.listp():
        r = []
        r.extend(flatten(sexp.first()))
        r.extend(flatten(sexp.rest()))
        return r
    return [sexp.as_atom()]


def build_used_constants_names(functions, constants, macros):
    """
    Do a naïve pruning of unused symbols. It may be too big, but it shouldn't
    be too small. Return a list of all atoms used that are also the names of
    functions or constants, starting with the MAIN_NAME function.
    """
    macros_as_dict = {_.rest().first().as_atom(): _ for _ in macros}

    possible_symbols = set(functions.keys())
    possible_symbols.update(constants.keys())

    new_names = set([MAIN_NAME])
    used_names = set(new_names)
    while new_names:
        prior_new_names = new_names
        new_names = set()
        for _ in prior_new_names:
            for k in [functions, macros_as_dict]:
                if _ in k:
                    new_names.update(flatten(k[_]))
        new_names.difference_update(used_names)
        used_names.update(new_names)
    used_names.intersection_update(possible_symbols)
    used_names.discard(MAIN_NAME)
    return sorted(used_names)


def parse_mod_sexp(declaration_sexp, namespace, functions, constants, macros):
    op = declaration_sexp.first().as_atom()
    name = declaration_sexp.rest().first().as_atom()
    if name in namespace:
        raise SyntaxError('symbol "%s" redefined' % name.decode())
    namespace.add(name)
    if op == b"defmacro":
        macros.append(declaration_sexp)
    elif op == b"defun":
        functions[name] = declaration_sexp.rest().rest()
    elif op == b"defconstant":
        constants[name] = [QUOTE_KW, declaration_sexp.rest().rest().first().as_atom()]
    else:
        raise SyntaxError("expected defun, defmacro, or defconstant")


def compile_mod_stage_1(args):
    """
    stage 1: collect up names of globals (functions, constants, macros)
    """

    functions = {}
    constants = {}
    macros = []
    main_local_arguments = args.first()

    namespace = set()
    while True:
        args = args.rest()
        if args.rest().nullp():
            break
        parse_mod_sexp(args.first(), namespace, functions, constants, macros)

    uncompiled_main = args.first()

    functions[MAIN_NAME] = args.to([main_local_arguments, uncompiled_main])

    return functions, constants, macros


def symbol_table_for_tree(tree, root_node):
    if tree.nullp():
        return []

    if not tree.listp():
        return [[tree, root_node.as_path()]]

    left = symbol_table_for_tree(tree.first(), root_node + LEFT)
    right = symbol_table_for_tree(tree.rest(), root_node + RIGHT)

    return left + right


def build_macro_lookup_program(macro_lookup, macros):
    macro_lookup_program = macro_lookup.to([QUOTE_KW, macro_lookup])
    for macro in macros:
        macro_lookup_program = eval(macro_lookup.to(
            [b"opt", [b"com", [QUOTE_KW, [CONS_KW, macro, macro_lookup_program]], macro_lookup_program]]),
            TOP.as_path())
    return macro_lookup_program


def compile_functions(functions, macro_lookup_program, constants_symbol_table, args_root_node):
    compiled_functions = {}
    for name, lambda_expression in functions.items():
        local_symbol_table = symbol_table_for_tree(lambda_expression.first(), args_root_node)
        all_symbols = local_symbol_table + constants_symbol_table
        compiled_functions[name] = lambda_expression.to(
            [b"opt", [b"com",
                      [QUOTE_KW, lambda_expression.rest().first()],
                      macro_lookup_program,
                      [QUOTE_KW, all_symbols]]])
    return compiled_functions


def compile_mod(args, macro_lookup, symbol_table):
    """
    Deal with the "mod" keyword.
    """
    (functions, constants, macros) = compile_mod_stage_1(args)

    # move macros into the macro lookup

    macro_lookup_program = build_macro_lookup_program(macro_lookup, macros)

    # get a list of all symbols that are possibly used

    all_constants_names = build_used_constants_names(functions, constants, macros)
    has_constants_tree = len(all_constants_names) > 0

    # build defuns table, with function names as keys

    constants_tree = args.to(build_tree(all_constants_names))

    constants_root_node = LEFT
    if has_constants_tree:
        args_root_node = RIGHT
    else:
        args_root_node = TOP

    constants_symbol_table = symbol_table_for_tree(constants_tree, constants_root_node)

    compiled_functions = compile_functions(
        functions, macro_lookup_program, constants_symbol_table, args_root_node)

    main_path_src = binutils.disassemble(compiled_functions[MAIN_NAME])

    if has_constants_tree:
        all_constants_lookup = dict(compiled_functions)
        all_constants_lookup.update(constants)

        all_constants_list = [all_constants_lookup[_] for _ in all_constants_names]
        all_constants_tree_program = args.to(build_tree_program(all_constants_list))

        all_constants_tree_src = binutils.disassemble(all_constants_tree_program)
        arg_tree_src = "(c %s (a))" % all_constants_tree_src
    else:
        arg_tree_src = "(a)"

    main_code = "(opt (q ((c %s %s))))" % (main_path_src, arg_tree_src)

    return binutils.assemble(main_code)
