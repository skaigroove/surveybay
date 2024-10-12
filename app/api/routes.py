from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def read_items():
    return {"items": ["item1", "item2", "item3"]}