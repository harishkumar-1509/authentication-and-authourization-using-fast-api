from app.models.user import User
from app.config.security import hash_password
from fastapi import HTTPException

async def create_user_account(data, session):
    
    user_exist = session.query(User).filter(User.email == data.email).first()
    if user_exist:
        raise HTTPException(status_code=400, details="Email already exists!")
    
    user = User()
    user.name = data.name
    user.email = data.email
    user.mobile_no = data.mobile_no
    user.password = hash_password(data.password)
    user.is_active = True
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user