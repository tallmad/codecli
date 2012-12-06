from __future__ import absolute_import

from commands import getoutput
from subprocess import check_call as _check_call

GREEN = '\x1b[1;32m'
RESET = '\x1b[0m'

def get_current_branch_name():
    output = getoutput('git symbolic-ref HEAD')
    assert output.startswith('refs/heads/')
    return output[len('refs/heads/'):]

def get_base_branch(branch):
    if branch.startswith('hotfix-'):
        return branch.split('-')[1]
    return 'master'

def merge_with_base(branch):
    base = get_base_branch(branch)
    check_call(['git', 'fetch', 'upstream'])
    check_call(['git', 'merge', 'upstream/%s' % base])


def check_call(cmd, *args, **kwargs):
    cmdstr = cmd if isinstance(cmd, basestring) else ' '.join(cmd)
    print GREEN + ">> " + cmdstr + RESET
    return _check_call(cmd, *args, **kwargs)
