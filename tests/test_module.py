import subprocess
import sys

import pytest

from gitfilesplit.cli import main
from gitfilesplit.toolbox import run, split


def test_basic(tmpdir):

    def add_change(*, fobj, text, msg):
        fobj.write(text)

        run(f'git add {fobj.basename}')
        run(f'git commit -m "{msg}"')

    with tmpdir.as_cwd():

        run('git init')
        source = tmpdir.join('myhugefile.py')

        base_text = '# this file has many files\n' * 80
        add_change(fobj=source, text=base_text, msg='first')

        add_change(
            fobj=source,
            text=f'{base_text}\nthis line is from commit 2',
            msg='second'
        )

        split(
            source=source.basename,
            targets=['sub/deep/smaller.py', 'sub2/another.py', 'sub/some.py']
        )
        result = subprocess.run('git log', shell=True, stdout=subprocess.PIPE)

        out = result.stdout
        assert b'Split myhugefile.py into sub/some.py' in out
        assert b'Split myhugefile.py into sub/deep/smaller.py' in out
        assert b'Split myhugefile.py into sub2/another.py' in out
        assert b'first' in out

        # todo maybe a cli test


def test_cli_requires_at_least_one_target(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['gitfilesplit', 'myhugefile.py'])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 2
    assert 'targets' in capsys.readouterr().err
