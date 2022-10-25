from typing import Any, Generic, Mapping, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.sql.expression import Executable

from app.repository.database import db

T = TypeVar("T", bound=db.Model)
M = TypeVar("M", bound=BaseModel)

Record = Mapping[Any, Any]
SAQuery = Executable


class BaseRepository(Generic[T, M]):
    table: Type[T]
    model: Type[M]

    @property
    def query(self) -> SAQuery:
        return self.table.query

    def record_to_instance(self, record: Record) -> M:
        return self.model(**record)

    def instance_to_dict(self, instance: M) -> dict[Any, Any]:
        dikt = instance.dict()
        if dikt.get("id", True) is None:
            dikt.pop("id")
        return dikt

    async def create(self, instance: M) -> M:
        query = (
            self.table.insert()
            .values(**self.instance_to_dict(instance))
            .returning(*self.table.__table__.c)
        )
        record = await query.gino.first()
        return self.record_to_instance(record)

    async def update(self, instance: M) -> M:
        ...

    async def delete(self, instance_id: int) -> None:
        ...

    async def retrieve(self, instance_id: int) -> M:
        ...
