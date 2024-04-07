from fastapi import APIRouter, Depends
from starlette import status
from app.responses.user import UserResponse
from app.schemas.user import RegisterUserRequest
from sqlalchemy.orm import Session
from app.config.database import get_session
from app.services import user

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
    responses={404: {'description': 'URL Not Found'}}
)

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(data: RegisterUserRequest, session: Session=Depends(get_session)):
    return await user.create_user_account(data, session)