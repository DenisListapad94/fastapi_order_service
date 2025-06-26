from pydantic import BaseModel

users = [
    {
        "id": 1,
        "email": "user_1",
        "first_name": "dsada",
        "last_name": "dsa",
        "is_superuser": False,
    },
    {
        "id": 6,
        "email": "user_2",
        "first_name": "dsada",
        "last_name": "dsada",
    },
    {
        "id": 3,
        "email": "user_3",
        "first_name": "dsada",
        "last_name": "dsada",
        "is_superuser": False,
        "is_active": True,
    },
]

class BaseUserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str

class UpdateUserSchema(BaseModel):
    first_name: str
    last_name: str

class CreateUserSchema(BaseUserSchema):
    pass

class UserListSchema(BaseUserSchema):
    id: int
    is_superuser: bool | None = None
    is_active: bool | None = None