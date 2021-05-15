from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve
from app.model_saver import MinioModelSaver


class Train():
    def model_fit(self):
        raise NotImplementedError

    def model_evaluate(self):
        raise NotImplementedError

    def model_save(self):
        raise NotImplementedError


class SklearnTrain(Train):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def model_fit(self):
        # TODO put hyperparameter here
        clf = LogisticRegression(random_state=0).fit(
            self.X_train, self.y_train)
        return clf

    def model_evaluate(self, model):
        predictions = model.predict_proba(self.X_test)[:, 1]

        # accuracy
        accuracy = model.score(self.X_test, self.y_test)

        # roc_auc
        fpr, tpr, _ = roc_curve(self.y_test, predictions)
        roc_auc = auc(fpr, tpr)

        # average_precision
        precision, recall, _ = precision_recall_curve(self.y_test, predictions)
        average_precision = auc(recall, precision)

        return {"accuracy": accuracy, "roc_auc": roc_auc, "average_precision": average_precision}

