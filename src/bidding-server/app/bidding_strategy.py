import requests
import json
from app.logger import get_logger

log = get_logger(logger_name="bidding_strategy")
class BiddingStrategy():
    def make_bid(self):
        raise NotImplementedError


class ClickPerCost(BiddingStrategy):
    def make_bid(self, ads_info, bid_request_info, ctr_info):
        price = 0
        ad_id = None
        for ad in ads_info:
            ad_price = ctr_info[ad["ad_id"]]*ad["bidding_cpc"]
            if ad_price > price:
                ad_id = ad["ad_id"]
                price = ad_price
        return {"price": price, "ad_id": ad_id}

    def get_ctr_prediction(self, ads_info, bid_request_info, model_uri):
        response = {}
        for ad in ads_info:
            data = {}
            data.update(ad)
            data.update(bid_request_info)
            del data["bid_floor"]
            r = requests.post(model_uri, json=data)
            # response["ad_id"] = json.loads(r.text)
            response[ad["ad_id"]] = r.json()["prediction"]
        return response
