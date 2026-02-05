from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Annotated
from ..schemas.user import UserCreate, UserLogin, Token, UserRead
from ..services.auth import create_user, authenticate_user_and_create_token
from ..config.database import get_session
from ..utils.auth import get_current_active_user
from ..models.user import User


router = APIRouter()


@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
def signup(user_create: UserCreate, session: Session = Depends(get_session)):
    """Register a new user"""
    # Check if user already exists
    existing_user = session.query(User).filter(User.email == user_create.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Create the user
    try:
        db_user = create_user(session, user_create)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create user: {str(e)}"
        )

    # Authenticate the user and create token
    token_data = authenticate_user_and_create_token(session, db_user.email, user_create.password)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )

    return {
        "access_token": token_data["access_token"],
        "token_type": token_data["token_type"]
    }


@router.post("/signin", response_model=Token)
def signin(user_login: UserLogin, session: Session = Depends(get_session)):
    """Authenticate user and return access token"""
    token_data = authenticate_user_and_create_token(session, user_login.email, user_login.password)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": token_data["access_token"],
        "token_type": token_data["token_type"]
    }


@router.get("/me", response_model=UserRead)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Get current user information"""
    return current_user