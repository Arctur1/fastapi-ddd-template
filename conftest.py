import pytest
from app.repository.database import db, close_db
from settings.settings import PROJECT_PATH, TEST_DB_URI
import asyncio
from alembic.config import main as run_alembic_command
async def init_test_db() -> None:
    await db.set_bind(TEST_DB_URI)


def upgrade_test_db() -> None:
    run_alembic_command(["-x", f"db_uri={TEST_DB_URI}","--raiseerr", "upgrade", "head"])

def downgrade_test_db() -> None:
    run_alembic_command(["-x", f"db_uri={TEST_DB_URI}","--raiseerr", "downgrade", "base"])


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup():
    upgrade_test_db()
    await init_test_db()
    yield

@pytest.fixture(scope="session", autouse=True)
async def teardown():
    yield
    await close_db()
    downgrade_test_db()