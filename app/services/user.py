from app.models.user import User

async def create_user_account(data, session):
    user = User()
    user.name = data.name
    user.email = data.email
    user.mobile_no = data.mobile_no
    user.password = data.password
    user.is_active = True
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user