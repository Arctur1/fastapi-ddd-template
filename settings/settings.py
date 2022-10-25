import pathlib
PROJECT_NAME: str = "example_app"
DB_NAME: str = PROJECT_NAME
DB_URI: str = "postgresql://admin:admin@postgres/example_app"
TEST_DB_URI: str = "postgresql://admin:admin@postgres/example_app_test"

PROJECT_PATH = pathlib.Path().absolute()