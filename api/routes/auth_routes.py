from core.database_connection import get_db
from schemas.auth.users_schema import RefreshRequest, TokenResponse, UserLogin
from fastapi import APIRouter, HTTPException
from repositories.auth.auth_repo import AuthRepository

router = APIRouter()


def get_auth_repo(db=next(get_db())):
    return AuthRepository(db)

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    print("login called")
    auth_repo : AuthRepository = get_auth_repo()
    try:
        tokens = auth_repo.authenticate_user(user)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Invalid email or password") from exc

    if tokens is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return tokens

@router.post('/refresh', response_model=TokenResponse)
def refresh_token(refresh_token: RefreshRequest):
    auth_repo : AuthRepository = get_auth_repo()
    return auth_repo.refresh_access_token(refresh_token.refresh_token)


@router.post('/logout')
def logout(refresh_token: RefreshRequest):
    auth_repo : AuthRepository = get_auth_repo()
    return auth_repo.revoke_refresh_token(refresh_token.refresh_token)
