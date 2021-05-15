from app.data_pipeline import PostgresDataPipeline
from tests.test_data.db_mocker import MockPostgresClient
from tests.test_data.test_data import test_records, test_formated_x, test_formated_y
from app.config import feature_mapping, target_features, data_columns
from unittest import TestCase
import psycopg2


class TestQueryElasticsearch(TestCase):

    pdp = PostgresDataPipeline(postgres_client=MockPostgresClient)
    # pdp = PostgresDataPipeline(postgres_client=psycopg2.connect(
    #     dbname="dsp",
    #     user="dsp",
    #     password="dsp",
    #     host="localhost",
    #     port="5432"))

    def test_get_records(self):
        res = self.pdp.records
        # assert res == test_records
        print(res)
        self.assertListEqual(res, test_records)

    def test_format_data(self):
        res_x, res_y = self.pdp.format_data(
            data_columns=data_columns,
            feature_mapping=feature_mapping, 
            target_feature=target_features)
        print(res_x, res_y)
        print(test_formated_y)
        assert res_x.equals(test_formated_x)
        assert res_y.equals(test_formated_y)
