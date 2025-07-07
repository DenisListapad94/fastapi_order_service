from fastapi import APIRouter, Depends,  status

from src.account.dependencies.user import get_user_service
from src.account.schemas.user import  (
    UserListSchema,
    CreateUserSchema,
    UpdateUserSchema,
)
from src.account.services.user import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/",
    response_model=list[UserListSchema],
    status_code=status.HTTP_200_OK,
    description = "Retrieve all users",
    responses={
        status.HTTP_200_OK: {
            "status_code": status.HTTP_200_OK,  # custom pydantic model for 200 response
            "description": "Ok Response",
        }
    }
)
async def get_users_handler(
    user_service: UserService = Depends(get_user_service)
):
    return await  user_service.get_all()


@router.post(
    "/",
    response_model=UserListSchema,
    status_code=status.HTTP_201_CREATED,
    description="Create new user",
    responses={
        status.HTTP_201_CREATED: {
            "status_code": status.HTTP_201_CREATED,  # custom pydantic model for 200 response
            "description": "Created Response",
        }
    }
)
async def create_user_handler(
        payload: CreateUserSchema,
        user_service: UserService = Depends(get_user_service)
):
    return await user_service.create(user_schema=payload)


@router.get(
    "/{user_id}",
    response_model=UserListSchema,
    status_code=status.HTTP_200_OK,
    description="Retrieve user by id",
    responses={
        status.HTTP_200_OK: {
            "status_code": status.HTTP_200_OK,  # custom pydantic model for 200 response
            "description": "Ok Response",
        }
    }
)
async def get_user_by_id_handler(
        user_id: int,
        user_service: UserService = Depends(get_user_service)
):
    return await  user_service.get_by_id(user_id=user_id)


@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserListSchema,
    description="Update user",
    responses={
        status.HTTP_200_OK: {
            "status_code": status.HTTP_200_OK,  # custom pydantic model for 200 response
            "description": "Ok Response",
        }
    }
)
async def update_user_by_id_handler(
    user_id: int,
    payload: UpdateUserSchema,
    user_service: UserService = Depends(get_user_service)
):
    return await  user_service.update(user_id=user_id, user_update_schema=payload)



@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete user",
    responses={
        status.HTTP_204_NO_CONTENT: {
            "status_code": status.HTTP_204_NO_CONTENT,  # custom pydantic model for 200 response
            "description": "No content Response",
        }
    }
)
async def delete_user_by_id_handler(
        user_id: int,
        user_service: UserService = Depends(get_user_service)
):
    await  user_service.delete(user_id=user_id)

