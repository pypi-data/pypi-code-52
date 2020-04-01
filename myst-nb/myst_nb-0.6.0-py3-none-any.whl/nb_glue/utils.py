import json
from pathlib import Path

import nbformat as nbf

from myst_nb.nb_glue import GLUE_PREFIX


def read_glue_cache(path):
    """Read a glue cache generated by Sphinx build.

    Parameters
    ----------
    path : str
        Path to a doctree dir, or directly to a glue cache .json file.

    Returns
    -------
    data : dictionary
        A dictionary containing the JSON data in your glue cache.
    """
    path = Path(path)
    if path.is_dir():
        # Assume our folder is doctrees and append the glue data name to it.
        path = path.joinpath("glue_cache.json")
    if not path.exists():
        raise FileNotFoundError(f"A glue cache was not found at: {path}")

    data = json.load(path.open())
    return data


def find_glued_key(path_ntbk, key):
    """Find an output mimebundle in a notebook based on a key.

    Parameters
    ----------
    path_ntbk : path
        The path to a Jupyter Notebook that has variables "glued" in it.
    key : string
        The unique string to use as a look-up in `path_ntbk`.

    Returns
    -------
    mimebundle
        The output mimebundle associated with the given key.
    """
    # Read in the notebook
    if isinstance(path_ntbk, Path):
        path_ntbk = str(path_ntbk)
    ntbk = nbf.read(path_ntbk, nbf.NO_CONVERT)
    outputs = []
    for cell in ntbk.cells:
        if cell.cell_type != "code":
            continue

        # If we have outputs, look for scrapbook metadata and reference the key
        for output in cell["outputs"]:
            meta = output.get("metadata", {})
            if "scrapbook" in meta:
                this_key = meta["scrapbook"]["name"].replace(GLUE_PREFIX, "")
                if key == this_key:
                    bundle = output["data"]
                    bundle = {this_key: val for key, val in bundle.items()}
                    outputs.append(bundle)
    if len(outputs) == 0:
        raise KeyError(f"Did not find key {this_key} in notebook {path_ntbk}")
    if len(outputs) > 1:
        raise KeyError(
            f"Multiple variables found for key: {this_key}. Returning first value."
        )
    return outputs[0]


def find_all_keys(ntbk, existing_keys=None, path=None, logger=None, strip_stored=True):
    """Find all `glue` keys in a notebook and return a dictionary with key: outputs.

    :param existing_keys: a map of key to docname
    :param strip_stored: if the content of a mimetype is already stored on disc
        (referenced in output.metadata.filenames) then replace it by None
    """
    if isinstance(ntbk, (str, Path)):
        ntbk = nbf.read(str(ntbk), nbf.NO_CONVERT)

    if existing_keys is None:
        existing_keys = {}
    new_keys = {}

    for i, cell in enumerate(ntbk.cells):
        if cell.cell_type != "code":
            continue

        for output in cell["outputs"]:
            meta = output.get("metadata", {})
            if "scrapbook" in meta:
                this_key = meta["scrapbook"]["name"]
                if this_key in existing_keys:
                    msg = (
                        f"Skipping glue key `{this_key}`, in cell {i}, "
                        f"that already exists in: '{existing_keys[this_key]}'"
                    )
                    if logger is None:
                        print(msg)
                    else:
                        logger.warning(msg, location=(path, None))
                    continue
                if this_key in new_keys:
                    msg = (
                        f"Glue key `{this_key}`, in cell {i}, overwrites one "
                        "previously defined in the notebook."
                    )
                    if logger is None:
                        print(msg)
                    else:
                        logger.warning(msg, location=(path, None))

                if strip_stored:
                    output = output.copy()
                    filenames = output["metadata"].get("filenames", {})
                    output["data"] = {
                        k: None if k.replace(GLUE_PREFIX, "") in filenames else v
                        for k, v in output.get("data", {}).items()
                    }

                new_keys[this_key] = output
    return new_keys
