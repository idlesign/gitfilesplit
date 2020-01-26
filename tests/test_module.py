from gitfilesplit.toolbox import run, split


def test_basic(tmpdir):

    def add_change(*, fobj, text, msg):
        fobj.write(text)

        run(f'git add {fobj.basename}')
        run(f'git commit -m "{msg}"')

    with tmpdir.as_cwd():

        run('git init')
        a = 1
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
            targets=['smaller.py', 'another.py', 'some.py']
        )

        # todo maybe a cli test
        # run('gitfilesplit myhugefile.py smaller.py another.py some.py ')
