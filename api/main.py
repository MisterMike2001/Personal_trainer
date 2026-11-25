from sqlalchemy import text
from core.database_connection import engine
from fastapi import FastAPI
from routes.auth_routes import router as auth_router

app = FastAPI(title="Personal Trainer API")


@app.get("/")
def root():
    return {"message": "Welcome to the Personal Trainer API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/connection/check")
def check_connection():

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "Database connection successful"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
