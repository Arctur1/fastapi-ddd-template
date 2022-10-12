from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    id: Optional[str]
    nickname: str
