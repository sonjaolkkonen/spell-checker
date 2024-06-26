from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/app.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
