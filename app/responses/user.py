from pydantic import BaseModel, EmailStr
from typing import Union
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    mobile_no: str
    is_active: bool
    created_at: Union[str, None, datetime] = None 