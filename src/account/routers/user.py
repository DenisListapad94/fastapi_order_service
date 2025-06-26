from fastapi import APIRouter, Depends, Body, HTTPException,status
from src.account.schemas.user import users, UserListSchema, CreateUserSchema, UpdateUserSchema
from src.account.services.user import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.orm import create_tables
from src.core.orm.db import get_sync_session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# def some_fun():
#     return {"limit":10,"offset":10}
#
# class Paginator:
#     def __init__(self):
#         self.limit = 10
#         self.offset = 1
#     def __call__(self, *args, **kwargs):
#         return {"limit":self.limit,"offset":self.offset}

# session: AsyncSession = Depends(get_sync_session)

@router.get("/", response_model=list[UserListSchema])
def get_users_handler(
    session: AsyncSession = Depends(get_sync_session)):
    user_service = UserService(session=session)
    return user_service.get_all()

@router.post("/", response_model=UserListSchema)
def create_user_handler(
    payload: CreateUserSchema,
    session: AsyncSession = Depends(get_sync_session),
):
    user_service = UserService(session=session)
    return user_service.create(user_schema=payload)


# @router.put("/", response_model=UserListSchema)
# def update_user_handler(
#         user_id: int = Query(),  # 1,3,6
#         payload: UpdateUserSchema
# ):
#     user = [user for user in users if user.get("id") == user_id][0]
#
#     user["first_name"] = payload.first_name
#     user["last_name"] = payload.last_name
#     return user
