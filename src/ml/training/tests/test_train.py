from app.train import SklearnTrain
from tests.test_data.test_data import test_formated_x, test_formated_y
from sklearn.linear_model._logistic import LogisticRegression
from unittest import TestCase


class TestSklearnTrain(TestCase):

    skt = SklearnTrain(
        X_train=test_formated_x,
        y_train=test_formated_y,
        X_test=test_formated_x,
        y_test=test_formated_y)

    def test_model(self):
        test_model = self.skt.model_fit()
        metrics = self.skt.model_evaluate(model=test_model)
        print(metrics)
        assert len(metrics.keys()) == 3 

    def test_model_save(self):
        test_model = self.skt.model_fit()
