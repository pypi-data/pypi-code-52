import logging
import os

import shortuuid

from dvc.exceptions import DvcException
from dvc.stage import Stage
from dvc.utils import resolve_output
from dvc.utils.fs import remove
from dvc.path_info import PathInfo

logger = logging.getLogger(__name__)


class GetDVCFileError(DvcException):
    def __init__(self):
        super().__init__(
            "the given path is a DVC-file, you must specify a data file "
            "or a directory"
        )


@staticmethod
def get(url, path, out=None, rev=None):
    from dvc.external_repo import external_repo

    out = resolve_output(path, out)

    if Stage.is_valid_filename(out):
        raise GetDVCFileError()

    # Creating a directory right beside the output to make sure that they
    # are on the same filesystem, so we could take the advantage of
    # reflink and/or hardlink. Not using tempfile.TemporaryDirectory
    # because it will create a symlink to tmpfs, which defeats the purpose
    # and won't work with reflink/hardlink.
    dpath = os.path.dirname(os.path.abspath(out))
    tmp_dir = os.path.join(dpath, "." + str(shortuuid.uuid()))
    try:
        with external_repo(url=url, rev=rev) as repo:
            if hasattr(repo, "cache"):
                repo.cache.local.cache_dir = tmp_dir

                # Try any links possible to avoid data duplication.
                #
                # Not using symlink, because we need to remove cache after we
                # are done, and to make that work we would have to copy data
                # over anyway before removing the cache, so we might just copy
                # it right away.
                #
                # Also, we can't use theoretical "move" link type here, because
                # the same cache file might be used a few times in a directory.
                repo.cache.local.cache_types = ["reflink", "hardlink", "copy"]

            repo.pull_to(path, PathInfo(out))
    finally:
        remove(tmp_dir)
