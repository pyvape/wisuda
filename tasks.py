from invoke import task


@task
def show_status(ctx):
    print('running')


@task
def waton(ctx):
    print('waton')
