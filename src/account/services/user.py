from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from src.account.models import User
from src.account.repositories.user import UserRepository
from src.account.schemas import CreateUserSchema, UpdateUserSchema


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = UserRepository(session=session)

    async def check_exist(self, email):
        if await self.repository.get_by_email(email=email):
            raise HTTPException(detail="OBJECT ALREADY EXIST", status_code=status.HTTP_409_CONFLICT)

    async def create(self, user_schema: CreateUserSchema):
        await self.check_exist(email=user_schema.email)
        return await self.repository.create(user_schema=user_schema)

    async def get_all(self) -> Sequence[User]:
        return await self.repository.get_list()

    async def get_by_id(self, user_id: int) -> User:
        user = await self.repository.get_by_id(user_id=user_id)
        if not user:
            raise HTTPException(detail="OBJECT NOT FOUND", status_code=status.HTTP_404_NOT_FOUND)
        return user

    async def update(
            self,
            user_id: int,
            user_update_schema: UpdateUserSchema
    ):
        user = await self.get_by_id(user_id=user_id)
        return await self.repository.update(
            user=user,
            user_update_schema=user_update_schema
        )

    async def delete(self, user_id):
        user = await self.get_by_id(user_id=user_id)
        await self.repository.delete(user=user)
