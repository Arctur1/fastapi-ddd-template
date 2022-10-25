from gino import Gino

from settings.settings import DB_URI

db = Gino()


async def init_db() -> None:
    await db.set_bind(DB_URI)


async def close_db() -> None:
    await db.pop_bind().close()
