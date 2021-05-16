from typing import Optional
from app.config import ModelInput, ModelOutput, HealthCheckOutput
from fastapi import FastAPI
from app.logger import get_logger
from app.utils import format_data

log = get_logger(logger_name="main")

app = FastAPI()
minio_client = Minio(
    minio_url,
    access_key=minio_access_key,
    secret_key=minio_secret_key,
    secure=False)
model = pickle.loads(client.get_object(bucket_name=bucket_name,
                               object_name=path_file).read())


@app.get("/health", response_model=HealthCheckOutput, tags=["Default"])
def health_check():
    return {"health": "True"}


@app.post("/model:predict", response_model=ModelOutput)
async def get_model_predict(data: ModelInput):
    try:
        formated_data = format_data(data.dict())
        prediction = model.predict_proba(formated_data)[0][0]
    except Exception as e:
        log.error("Error in makeing prediction: {}".format(e))
        prediction = 0.009905203839797677

    return {"prediction": prediction}


@app.put("/model")
async def update_model():
    pass


if __name__ == "__main__":
    uvicorn.run(app=app)
