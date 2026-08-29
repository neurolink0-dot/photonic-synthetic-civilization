from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)
from api_karma import router as karma_router
app.include_router(karma_router)
