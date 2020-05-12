"""
tasks.test contains unit testing tasks description.
"""

from invoke import task

from tasks.common import PIPENV_PREFIX


@task
def pytest(ctx):
    """
    run unit test through pytest.
    """
    ctx.run('{PREFIX} pytest'.format(
        PREFIX=PIPENV_PREFIX
    ))
