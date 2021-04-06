import click


@click.group()
def cli():
    pass


@cli.command()
def joint():
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


