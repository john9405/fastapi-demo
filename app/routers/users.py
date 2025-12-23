from typing import Annotated

from fastapi import APIRouter, Depends

from ..dependencies import get_current_active_user
from ..models import User

router = APIRouter()

@router.get("/users/me", tags=["users"], response_model=User)
async def read_user_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

    