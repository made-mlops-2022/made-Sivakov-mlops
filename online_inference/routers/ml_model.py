from fastapi import APIRouter, HTTPException, UploadFile, File
from online_inference.schemas.ml_model import HealthChecker
from online_inference.model import prediction_process
import pandas as pd
from io import BytesIO


router = APIRouter()


@router.get("/")
async def hello_world():
    return 'hello world'


@router.post("/predict")
async def predict(file: UploadFile):
    content = await file.read()
    df = pd.read_csv(BytesIO(content))
    predictions = prediction_process.start(df)

    return {'predictions': pd.Series(predictions).to_json(orient='values')}


@router.get("/health", tags=['model'], response_model=HealthChecker)
async def health():
    health_response = {"health": prediction_process.health_checker()}

    if not health_response["health"]:
        raise HTTPException(status_code=401, detail='model is not alive')

    return health_response
