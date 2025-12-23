from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_current_active_user
from ..models import User
from ..fake_db import fake_items_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_items(
        current_user: Annotated[User, Depends(get_current_active_user)],
):
    return fake_items_db


@router.get("/{item_id}")
async def read_item(
        item_id: str,
        current_user: Annotated[User, Depends(get_current_active_user)],
):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(
        item_id: str,
        current_user: Annotated[User, Depends(get_current_active_user)],
):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
