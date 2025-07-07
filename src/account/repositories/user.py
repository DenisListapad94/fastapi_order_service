from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from src.account.schemas import CreateUserSchema, UpdateUserSchema
from src.account.models import User
from sqlalchemy import select


class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_schema: CreateUserSchema) -> User:
        user = User(
            first_name=user_schema.first_name,
            last_name=user_schema.last_name,
            email=user_schema.email,
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.flush()
        return user

    async def update(
        self,
        user: User,
        user_update_schema: UpdateUserSchema,
    ) -> User:
        for name, value in user_update_schema.model_dump().items():
            setattr(user,name,value)
        await self.session.commit()
        await self.session.flush()
        return user

    async def delete(self, user: User):
        await self.session.delete(user)
        await self.session.commit()

    async def get_by_id(self, user_id: int) -> User:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def get_list(self) -> Sequence[User]:
        query = select(User)
        result = await self.session.execute(query)
        return result.scalars().all()
