"""
Implements integration of jupyter-cache
"""
import os
import nbformat as nbf
from nbclient import execute
from pathlib import Path

from sphinx.util import logging
from sphinx.util.osutil import ensuredir

from jupyter_cache import get_cache
from jupyter_cache.executors import load_executor

LOGGER = logging.getLogger(__name__)


def is_valid_exec_file(env, docname):
    """Check if the docname refers to a file that should be executed."""
    doc_path = env.doc2path(docname)
    if doc_path in env.excluded_nb_exec_paths:
        return False
    extension = os.path.splitext(doc_path)[1]
    if extension not in env.allowed_nb_exec_suffixes:
        return False
    return True


def execution_cache(app, builder, added, changed, removed):
    """
    If caching is required, stages and executes the added or modified notebooks,
    and caches them for further use.
    """
    jupyter_cache = False

    # all the added and changed notebooks should be operated on.
    # note docnames are paths relative to the sphinx root folder, with no extensions
    altered_docnames = added.union(changed)

    if app.config["jupyter_execute_notebooks"] not in ["force", "auto", "cache", "off"]:
        LOGGER.error(
            "Conf jupyter_execute_notebooks can either be `force`, `auto`, `cache` or `off`"  # noqa: E501
        )
        exit(1)

    jupyter_cache = app.config["jupyter_cache"]

    exec_list = [
        docname for docname in altered_docnames if is_valid_exec_file(app.env, docname)
    ]
    LOGGER.verbose("MyST-NB: Potential docnames to execute: %s", exec_list)

    if "cache" in app.config["jupyter_execute_notebooks"]:
        if jupyter_cache:
            if os.path.isdir(jupyter_cache):
                path_cache = jupyter_cache
            else:
                LOGGER.error(
                    f"Path to jupyter_cache is not a directory: {jupyter_cache}"
                )
                exit(1)
        else:
            path_cache = Path(app.outdir).parent.joinpath(".jupyter_cache")

        app.env.path_cache = str(
            path_cache
        )  # TODO: is there a better way to make it accessible?

        cache_base = get_cache(path_cache)
        for path in removed:
            docpath = app.env.doc2path(path)
            # there is an issue in sphinx doc2path, whereby if the path does not
            # exist then it will be assigned the default source_suffix (usually .rst)
            # therefore, to be safe here, we run through all possible suffixes
            for suffix in app.env.allowed_nb_exec_suffixes:
                docpath = os.path.splitext(docpath)[0] + suffix
                cache_base.discard_staged_notebook(docpath)

        _stage_and_execute(app, exec_list, path_cache)

    elif jupyter_cache:
        LOGGER.error(
            "If using conf jupyter_cache, please set jupyter_execute_notebooks"  # noqa: E501
            " to `cache`"
        )
        exit(1)

    return altered_docnames


def _stage_and_execute(app, exec_list, path_cache):
    pk_list = None

    cache_base = get_cache(path_cache)

    for nb in exec_list:
        if "." in nb:  # nb includes the path to notebook
            source_path = nb
        else:
            source_path = app.env.doc2path(nb)

        if pk_list is None:
            pk_list = []
        stage_record = cache_base.stage_notebook_file(source_path)
        pk_list.append(stage_record.pk)

    # can leverage parallel execution implemented in jupyter-cache here
    execute_staged_nb(cache_base, pk_list)


def add_notebook_outputs(env, ntbk, file_path=None):
    """
    Add outputs to a NotebookNode by pulling from cache.

    Function to get the database instance. Get the cached output of the notebook
    and merge it with the original notebook. If there is no cached output,
    checks if there was error during execution, then saves the traceback to a log file.
    """
    # If we have a jupyter_cache, see if there's a cache for this notebook
    file_path = file_path or env.doc2path(env.docname)
    dest_path = Path(env.app.outdir)
    reports_dir = str(dest_path) + "/reports"
    path_cache = False

    if not is_valid_exec_file(env, env.docname):
        return ntbk

    if "cache" in env.config["jupyter_execute_notebooks"]:
        path_cache = env.path_cache

    if not path_cache:
        if "off" not in env.config["jupyter_execute_notebooks"]:
            has_outputs = _read_nb_output_cells(
                file_path, env.config["jupyter_execute_notebooks"]
            )
            if not has_outputs:
                LOGGER.info("Executing: {}".format(env.docname))
                ntbk = execute(ntbk)
            else:
                LOGGER.info(
                    "Did not execute {}. "
                    "Set jupyter_execute_notebooks to `force` to execute".format(
                        env.docname
                    )
                )
        return ntbk

    cache_base = get_cache(path_cache)
    r_file_path = Path(file_path).relative_to(Path(file_path).cwd())

    try:
        _, ntbk = cache_base.merge_match_into_notebook(ntbk)
    except KeyError:
        message = (
            f"Couldn't find cache key for notebook file {str(r_file_path)}. "
            "Outputs will not be inserted."
        )
        try:
            stage_record = cache_base.get_staged_record(file_path)
        except KeyError:
            stage_record = None
        if stage_record and stage_record.traceback:
            # save the traceback to a log file
            ensuredir(reports_dir)
            file_name = os.path.splitext(r_file_path.name)[0]
            full_path = reports_dir + "/{}.log".format(file_name)
            with open(full_path, "w") as log_file:
                log_file.write(stage_record.traceback)
            message += "\n  Last execution failed with traceback saved in {}".format(
                full_path
            )

        LOGGER.error(message)
    else:
        LOGGER.verbose("Merged cached outputs into %s", str(r_file_path))

    return ntbk


def execute_staged_nb(cache_base, pk_list):
    """
    executing the staged notebook
    """
    try:
        executor = load_executor("basic", cache_base, logger=LOGGER)
    except ImportError as error:
        LOGGER.error(str(error))
        return 1
    result = executor.run_and_cache(filter_pks=pk_list or None)
    return result


def _read_nb_output_cells(source_path, jupyter_execute_notebooks):
    has_outputs = False
    if jupyter_execute_notebooks and jupyter_execute_notebooks == "auto":
        with open(source_path, "r") as f:
            ntbk = nbf.read(f, as_version=4)
            has_outputs = all(
                len(cell.outputs) != 0
                for cell in ntbk.cells
                if cell["cell_type"] == "code"
            )
    return has_outputs
