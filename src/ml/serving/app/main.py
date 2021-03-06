from typing import Optional
from app.config import ModelInput, ModelOutput, HealthCheckOutput, minio_server_info, default_ctr
from fastapi import FastAPI
from app.logger import get_logger
from app.utils import format_data
from minio import Minio
import pickle

log = get_logger(logger_name="main")

app = FastAPI()
log.fatal("minio server info : {}".format(minio_server_info))
minio_client = Minio(
    minio_server_info["uri"],
    access_key=minio_server_info["access_key"],
    secret_key=minio_server_info["secret_key"],
    secure=False)
model = pickle.loads(
    minio_client.get_object(
        bucket_name="default-model",
        object_name="model.pickle").read())


@app.get("/health", response_model=HealthCheckOutput)
def health_check():
    return {"health": "True"}


@app.post("/model:predict", response_model=ModelOutput)
def get_model_predict(data: ModelInput):
    try:
        formated_data = format_data(data.dict())
        prediction = model.predict_proba(formated_data)[0][0]
    except Exception as e:
        log.error("Error in makeing prediction: {}".format(e))
        prediction = default_ctr

    return {"prediction": prediction}


@app.put("/model")
def update_model():
    pass


if __name__ == "__main__":
    uvicorn.run(app=app)
