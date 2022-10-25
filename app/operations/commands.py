import click
import uvicorn


@click.group()
def cli() -> None:
    pass


@cli.command()
def run_server() -> None:
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, log_level="info")
