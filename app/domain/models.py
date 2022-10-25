from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    id: Optional[str] = None
    nickname: str

    class Config:
        orm_mode = True
