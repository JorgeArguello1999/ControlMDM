from fastapi import FastAPI
from auth.routes import router as auth_router

app = FastAPI()

# Registering routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}