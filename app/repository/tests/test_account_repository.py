from app.domain.models import Account
from app.repository.account_repository import AccountRepository


async def test_account_repo() -> None:
    account = Account(nickname="test")
    result = await AccountRepository().create(account)
    assert result == account
