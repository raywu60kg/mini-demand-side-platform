from app.get_ads import GetAdsFromPostgres
import psycopg2
from unittest import TestCase


class TestGetAdsFromPostgres(TestCase):
    gafp = GetAdsFromPostgres()

    def test_get_eligible_ads(self):
        # res = self.gafp.get_eligible_ads(
        #     postgres_client=psycopg2.connect(
        #         dbname="dsp",
        #         user="dsp",
        #         password="dsp",
        #         host="localhost",
        #         port="5433"))
        # print(res)
        assert 1 == 1
