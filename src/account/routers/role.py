from fastapi import APIRouter

router = APIRouter(
    prefix="/roles",
    tags = ["Roles"]
)


@router.get("/")
def read_roles():
    return {"Hello": "World"}


