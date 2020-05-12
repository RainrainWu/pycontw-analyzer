"""
tasks.env contains environment setup tasks description.
"""

from invoke import task


@task
def clean(ctx):
    """
    remove virtual environement.
    """
    ctx.run("pipenv --rm", warn=True)


@task
def init(ctx):
    """
    install production dependencies.
    """
    ctx.run("pipenv install --deploy")
