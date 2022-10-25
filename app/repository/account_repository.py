from app.domain.models import Account
from app.repository.base import BaseRepository
from app.repository.tables import AccountModel


class AccountRepository(BaseRepository[AccountModel, Account]):
    table = AccountModel
    model = Account
