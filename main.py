from fastapi import FastAPI
from online_inference.routers.ml_model import router

app = FastAPI()
app.include_router(router)
