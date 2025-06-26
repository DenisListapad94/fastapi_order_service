from sqlalchemy.ext.asyncio import AsyncSession

from src.account.repositories.user import UserRepository
from src.account.schemas import CreateUserSchema


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = UserRepository(session=session)

    def create(self, user_schema: CreateUserSchema):
        return self.repository.create(user_schema=user_schema)

    def get_all(self):
        return self.repository.get_list()