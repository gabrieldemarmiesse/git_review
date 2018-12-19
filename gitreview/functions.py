import subprocess
import click
import os


class BashError(Exception):
    pass


def cmd(string, fail_ok=False):
    if isinstance(string, str):
        string = string.split()

    print('calling ', ' '.join(string))

    a = subprocess.call(string)
    if a != 0 and not fail_ok:
        raise BashError('return code: ' + str(a))


@click.command()
@click.argument('username_branch')
@click.option('--conflicts', is_flag=True)
def pull_branch(username_branch, conflicts):
    repo = os.path.realpath('./').split('/')[-1]
    username, branch_name = username_branch.split(':')
    cmd('git pull')
    cmd('git pull upstream master')
    local_branch = f'{username}_{branch_name}'
    try:
        cmd(f'git checkout {local_branch}')
        cmd('git merge master --no-edit')
    except BashError:
        cmd(f'git checkout -b {local_branch}')

    cmd(f'git remote add {username} git@github.com:{username}/{repo}.git',
        fail_ok=True)
    if conflicts:
        cmd(f'git pull {username} {branch_name}')
    else:
        cmd(f'git pull {username} {branch_name} --no-edit')
        try:
            cmd(f'git push')
        except BashError:
            cmd(f'git push --set-upstream origin {local_branch}')
