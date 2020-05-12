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


@task
def flake8(ctx):
    """
    check style throug flake8.
    """
    ctx.run('{PREFIX} flake8'.format(
        PREFIX=PIPENV_PREFIX
    ))


@task
def mypy(ctx):
    """
    check style through mypy.
    """
    ctx.run('{PREFIX} mypy {MODULE}'.format(
        PREFIX=PIPENV_PREFIX,
        MODULE=MODULE_NAME
    ))


@task
def blackcheck(ctx):
    """
    check style through black.
    """
    ctx.run("{PREFIX} black --check {MODULE}".format(
        PREFIX=PIPENV_PREFIX,
        MODULE=MODULE_NAME
    ))


@task
def black(ctx):
    """
    fix style through black.
    """
    ctx.run("{PREFIX} black {MODULE}".format(
        PREFIX=PIPENV_PREFIX,
        MODULE=MODULE_NAME
    ))
