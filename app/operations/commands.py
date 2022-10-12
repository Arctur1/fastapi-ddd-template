import click
import uvicorn


@click.group()
def cli():
    pass


@cli.command()
def run_server():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, log_level="info")
