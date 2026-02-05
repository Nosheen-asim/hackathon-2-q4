from sqlmodel import Session, select
from typing import Optional
from datetime import timedelta
from ..models.user import User, UserCreate
from ..utils.security import get_password_hash
from ..config.settings import settings
from ..utils.auth import create_access_token


def create_user(session: Session, user_create: UserCreate) -> User:
    """Create a new user"""
    # Hash the password
    hashed_password = get_password_hash(user_create.password)

    # Create the user object
    db_user = User(
        email=user_create.email,
        hashed_password=hashed_password
    )

    # Add to session and commit
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def authenticate_user_and_create_token(session: Session, email: str, password: str) -> Optional[dict]:
    """Authenticate user and create access token"""
    from ..utils.auth import authenticate_user

    user = authenticate_user(session, email, password)
    if not user:
        return None

    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {
        "user": user,
        "access_token": access_token,
        "token_type": "bearer"
    }