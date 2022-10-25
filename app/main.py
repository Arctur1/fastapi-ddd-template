from fastapi import FastAPI

from app.handlers import api_router
from app.repository.database import close_db, init_db

app: FastAPI = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
async def _on_startup() -> None:
    await init_db()


@app.on_event("shutdown")
async def _on_shutdown() -> None:
    await close_db()
