import logging
import os

from dvc.compat import fspath
from dvc.exceptions import CheckoutError
from dvc.exceptions import CheckoutErrorSuggestGit
from dvc.progress import Tqdm
from dvc.utils import relpath

logger = logging.getLogger(__name__)


def _get_unused_links(repo):
    used = [
        out.fspath
        for stage in repo.stages
        for out in stage.outs
        if out.scheme == "local"
    ]
    return repo.state.get_unused_links(used)


def _fspath_dir(path, root):
    if not os.path.exists(str(path)):
        return str(path)

    path = relpath(fspath(path), root)
    return os.path.join(path, "") if os.path.isdir(path) else path


def get_all_files_numbers(pairs):
    return sum(
        stage.get_all_files_number(filter_info) for stage, filter_info in pairs
    )


def _checkout(
    self,
    targets=None,
    with_deps=False,
    force=False,
    relink=False,
    recursive=False,
):
    from dvc.stage import StageFileDoesNotExistError, StageFileBadNameError

    unused = []
    stats = {
        "added": [],
        "deleted": [],
        "modified": [],
        "failed": [],
    }
    if not targets:
        targets = [None]
        unused = _get_unused_links(self)

    stats["deleted"] = [_fspath_dir(u, self.root_dir) for u in unused]
    self.state.remove_links(unused)

    pairs = set()
    for target in targets:
        try:
            pairs.update(
                self.collect_granular(
                    target, with_deps=with_deps, recursive=recursive
                )
            )
        except (StageFileDoesNotExistError, StageFileBadNameError) as exc:
            if not target:
                raise
            raise CheckoutErrorSuggestGit(target) from exc

    total = get_all_files_numbers(pairs)
    with Tqdm(
        total=total, unit="file", desc="Checkout", disable=total == 0
    ) as pbar:
        for stage, filter_info in pairs:
            result = stage.checkout(
                force=force,
                progress_callback=pbar.update_desc,
                relink=relink,
                filter_info=filter_info,
            )
            for data in ["failed", "added", "modified"]:
                stats[data].extend(
                    _fspath_dir(path, self.root_dir) for path in result[data]
                )

    if stats.get("failed"):
        raise CheckoutError(stats["failed"], stats)

    del stats["failed"]
    return stats
