from app.logger import get_logger
from app.train import SklearnTrain
from app.data_pipeline import PostgresDataPipeline
from app.model_saver import MinioModelSaver
from app.config import (
    train_method,
    data_pipeline_method,
    model_saver_method,
    postgres_server_info,
    minio_server_info,
    data_columns,
    target_features,
    feature_mapping)
from datetime import datetime
from fastapi import FastAPI
from fastapi import BackgroundTasks
from typing import Optional
from minio import Minio
import psycopg2

log = get_logger(logger_name="main")

app = FastAPI()


@app.post("/train/")
async def train_model(background_tasks: BackgroundTasks):
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    log.info("Start training at {}".format(dt_string))
    try:
        if data_pipeline_method == "postgres":
            postgres_client = psycopg2.connect(
                dbname=postgres_server_info["dbname"],
                user=postgres_server_info["user"],
                password=postgres_server_info["password"],
                host=postgres_server_info["host"],
                port=postgres_server_info["port"])
            pdp = PostgresDataPipeline(postgres_client=postgres_client)
            pdp.format_data(
                data_columns=data_columns,
                target_features=target_features,
                feature_mapping=feature_mapping)
            X_train, y_train = pdp.get_training_data()
            X_test, y_test = pdp.get_testing_data()

        else:
            return(
                "Not support data_pipeline_method: {}".format(
                    data_pipeline_method)
            )
    except Exception as e:
        log.error("Data Pipeline error: {}".format(e))
        return "Data pipeline error: {}".format(e)
    try:
        if train_method == "sklearn":
            skt = SklearnTrain(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test)
            model = skt.model_fit()
            model_metrics = skt.model_evaluate(model=model)
        else:
            return "Not support train_method: {}".format(train_method)
    except Exception as e:
        log.error("Train model error: {}".format(e))
        return "Model training error {}".format(e)

    try:
        if model_saver_method == "minio":
            minio_client = Minio(
                minio_server_info["uri"],
                minio_server_info["access_key"],
                minio_server_info["secret_key"],
                secure=False)
            mms = MinioModelSaver(minio_client=minio_client)
            mms.save(
                model=model,
                model_metrics=model_metrics,
                bucket_name="model-"+dt_string)
        else:
            return(
                "Not support model_saver_method: {}".format(
                    model_saver_method)
            )
    except Exception as e:
        log.error("Save model error: {}".format(e))
        return "Save model error {}".format(e)
    return {"model": True}


@app.get("/model_list/")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/serving_model")
def update_serving_model(model_bucket_name: str):
    return{"hi": "there"}


@app.get("/health")
def health_check():
    return {"health": "True"}


if __name__ == "__main__":
    uvicorn.run(app=app)
