from app.bidding_strategy import ClickPerCost
from tests.test_data.test_ads import test_ads_info, test_bid_request_info, test_ctr_info
from unittest import TestCase


class TestClickPerCost(TestCase):
    cpc = ClickPerCost()

    def test_get_ctr_prediction(self):
        res = self.cpc.get_ctr_prediction(
            ads_info=test_ads_info,
            bid_request_info=test_bid_request_info,
            model_uri="http://localhost:8000/model:predict")
        print(res)
        assert 1 == 2

    # def test_make_bid(self):
    #     res = self.cpc.make_bid(
    #         ads_info=test_ads_info,
    #         bid_request_info=test_bid_request_info,
    #         ctr_info=test_ctr_info)
    #     print(res)
    #     assert 1 == 2
