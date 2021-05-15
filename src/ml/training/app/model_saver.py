from minio import Minio
import io
import json
import pickle


class ModelSaver():
    def save(self):
        raise NotImplementedError


class MinioModelSaver(ModelSaver):
    def __init__(self, minio_client):
        self.minio_client = minio_client

    def save(self, model, model_metrics, bucket_name):
        buckets = self.minio_client.list_buckets()
        for bucket in buckets:
            print(bucket.name, bucket.creation_date)

        self.minio_client.make_bucket(bucket_name)

        # save model metrics
        data = json.dumps(model_metrics).encode("utf-8")
        data_stream = io.BytesIO(data)
        # data_stream.seek(0)

        # put data as object into the bucket
        self.minio_client.put_object(
            bucket_name=bucket_name,
            object_name="metrics.json",
            data=data_stream,
            length=len(data)
        )

        # save model
        data = pickle.dumps(model)
        data_stream = io.BytesIO(data)

        self.minio_client.put_object(
            bucket_name=bucket_name,
            object_name="model.pickle",
            data=data_stream,
            length=len(data)
        )
