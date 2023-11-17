import click
from src.modules.analyze.links import analyze_links
from src.modules.keyword.keywords import get_volume

@click.group()
def cli():
    pass


@click.command("analyze")
@click.argument('url', type=str)
@click.option('--css-class', type=str, help="The class to find in", required=False)
@click.option('--id', type=str, help="The ID to find in", required=False)
def analyze(url, css_class, id):
    """Analyze an URL and returns relevant informations such as word count, internal and external links."""
    analyze_links(url, css_class, id)


@click.command("kw")
@click.argument('kw', type=str)
@click.option('--locale', type=str, help="Restrict the data to a specific language.", required=False)
def kw(kw, locale):
    get_volume(kw, locale.upper())




cli.add_command(analyze)
cli.add_command(kw)


if __name__ == '__main__':
    cli()