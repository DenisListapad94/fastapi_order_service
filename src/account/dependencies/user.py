from fastapi import Depends

from src.account.services.user import UserService
from src.core.orm.db import get_async_session
from sqlalchemy.ext.asyncio import  AsyncSession

async def get_user_service(
        session: AsyncSession = Depends(get_async_session),
):
    return UserService(session=session)
