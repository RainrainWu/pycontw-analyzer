"""
tasks.style contains coding style checking tasks description.
"""

from invoke import task

from tasks.common import (
    PIPENV_PREFIX,
    MODULE_NAME,
)


@task
def pylint(ctx):
    """
    check style through pylint.
    """
    ctx.run('{PREFIX} pylint {MODULE}'.format(
        PREFIX=PIPENV_PREFIX,
        MODULE=MODULE_NAME
    ))
