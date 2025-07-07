from pydantic import BaseModel

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