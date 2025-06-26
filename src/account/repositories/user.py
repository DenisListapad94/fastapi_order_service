from sqlalchemy.ext.asyncio import AsyncSession

from src.account.schemas import CreateUserSchema
from src.account.models import User
from sqlalchemy import Select

class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    def create(self,user_schema : CreateUserSchema):
        user = User(
            first_name=user_schema.first_name,
            last_name=user_schema.last_name,
            email=user_schema.email,
        )
        self.session.add(user)
        self.session.commit()
        return user

    def update(self):
        pass

    def get(self):
        pass

    def get_list(self):
        query = Select(User)
        result = self.session.scalars(query)
        return result
