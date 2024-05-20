from fastapi import APIRouter

router = APIRouter(
    prefix="/test"
)

@router.get("/")
def read_root():
    return {"Hello": "World"}
