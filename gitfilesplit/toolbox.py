import logging
from os import makedirs
from pathlib import Path
from subprocess import run as run_
from typing import List

LOG = logging.getLogger(__name__)


def run(command: str, *, check_code: bool = True):
    result = run_(command, shell=True)
    check_code and result.check_returncode()
    return result


def split(*, source: str, targets: List[str]):
    """Splits one file into several

    :param source: Source file name

    :param targets: Target file names (may include subdirectories).

        Examples:
            * myfile.py
            * subdir/deeper/another.py

    """
    LOG.info(f"Splitting {source} into {', '.join(targets)}")

    total = len(targets)
    branches = []

    try:

        for idx, target in enumerate(targets, 1):

            LOG.info(f"Split out {source} into {target} ...")

            branch_name = f'split/{source}-{target}'

            is_last = idx == total

            if not is_last:
                run(f'git checkout -b {branch_name}')
                branches.append(branch_name)

            parent = Path(target).parent
            if parent:
                makedirs(f'{parent}', exist_ok=True)

            run(f'git mv {source} {target}')

            run(f'echo " " >> {target}')  # This satisfies octopus merge.

            run(f'git add {target}')
            run(f'git commit -m "Split {source} into {target}"')

            if not is_last:
                run('git checkout -')

        if branches:

            run(f"git merge {' '.join(branches)}")

    finally:

        for branch in branches:
            run(f'git branch -D {branch}', check_code=False)

    LOG.info("Done split")
