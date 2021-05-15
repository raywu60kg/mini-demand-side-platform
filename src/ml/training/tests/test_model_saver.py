from unittest import TestCase
from sklearn.linear_model import LogisticRegression
from app.model_saver import MinioModelSaver
from minio import Minio


class TestMinioModelSaver(TestCase):

    client = Minio("localhost:9000", "dsp", "00000000",secure=False)
    mms = MinioModelSaver(minio_client=client)

    def test_save(self):
        test_model = LogisticRegression()
        self.mms.save(model=test_model, model_metrics={"test":123}, bucket_name="test")
        assert 1 == 1