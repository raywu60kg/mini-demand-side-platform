from app.logger import get_logger
import io
import json
import pickle

log = get_logger(logger_name="model_saver")


class ModelSaver():
    def save(self):
        raise NotImplementedError


class MinioModelSaver(ModelSaver):
    def __init__(self, minio_client):
        self.minio_client = minio_client

    def save(self, model, model_metrics, bucket_name):

        if self.minio_client.bucket_exists("my-bucket"):
            print("my-bucket exists")
        else:
            print("my-bucket does not exist")
            self.minio_client.make_bucket(bucket_name)

        # save model metrics
        try:
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
            log.info("Saved model metrics")
        except Exception as e:
            log.error("Save model metrics error: {}".format(e))

        # save model
        try:
            data = pickle.dumps(model)
            data_stream = io.BytesIO(data)

            self.minio_client.put_object(
                bucket_name=bucket_name,
                object_name="model.pickle",
                data=data_stream,
                length=len(data)
            )
        except Exception as e:
            log.error("Save model error: {}".format(e))


class LocalModelSaver(ModelSaver):
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def save(self, model, model_metrics):
        if os.path.isdir(output_dir):
            log.info("output dir exist")
        else:
            os.mkdir(self.output_dir)

        # save model metrics
        with open(os.path.join(self.output_dir, "model_metrics.json"), "w") as f:
            json.dump(model_metrics, f)

        # save model
        with open(os.path.join(self.output_dir, "model.pickle"), "wb") as f:
            pickle.dump(model, f)
