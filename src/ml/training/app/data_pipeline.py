import psycopg2
import pandas as pd
from sklearn.model_selection import train_test_split


class DataPipeline():
    def get_training_data(self):
        raise NotImplementedError

    def get_testing_data(self):
        raise NotImplementedError


class PostgresDataPipeline(DataPipeline):
    def __init__(self, postgres_client):
        conn = postgres_client

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a query
        cur.execute("SELECT * FROM ctr;")

        # Retrieve query results
        self.records = cur.fetchall()

    def format_data(self, data_columns, target_feature, feature_mapping):
        records_df = pd.DataFrame(
            self.records,
            columns=data_columns
        )

        # training feature
        formated_data = {}
        for key, value in feature_mapping.items():
            sub_key = list(value.keys())[0]

            # numerical_features
            if value[sub_key] is None:
                formated_data = records_df[sub_key]
            # categorical_features
            else:
                column = list(
                    map(lambda x: 1 if x == value[sub_key] else 0, records_df[sub_key]))
                formated_data[key] = column

        X, y = pd.DataFrame(formated_data), records_df[target_feature]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)
        return X, y

    def get_training_data(self):
        return self.X_train, self.y_train

    def get_testing_data(self):
        return self.X_test, self.y_test
