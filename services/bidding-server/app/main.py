from typing import Optional
from app.config import RequestInput, RequestOutput, HealthCheckOutput, bidding_strategy, get_ads_method, postgres_server_info, model_uri
from fastapi import FastAPI, status, Response
from app.logger import get_logger
from fastapi.responses import JSONResponse
from app.bidding_strategy import ClickPerCost
from app.get_ads import GetAdsFromPostgres
import psycopg2

log = get_logger(logger_name="main")

app = FastAPI()


@app.get("/health", response_model=HealthCheckOutput)
def health_check():
    return {"health": "True"}


@app.post("/bw_dsp")
# @app.post("/bw_dsp", response_model=RequestOutput)
def handle_bid_request(bid_request: RequestInput):

    # get ads
    try:
        if get_ads_method == "postgres":
            postgres_client = psycopg2.connect(
                dbname=postgres_server_info["dbname"],
                user=postgres_server_info["user"],
                password=postgres_server_info["password"],
                host=postgres_server_info["host"],
                port=postgres_server_info["port"])
            gafp = GetAdsFromPostgres()
            ads_info = gafp.get_eligible_ads(postgres_client=postgres_client)
    except Exception as e:
        log.error("Get ads error: {}".format(e))

    try:
        if bidding_strategy == "cpc":
            cpc = ClickPerCost()
            ctr_info = cpc.get_ctr_prediction(
                ads_info=ads_info,
                bid_request_info=bid_request, 
                model_uri=model_uri)
            log.info("ctr_info {}".format(ctr_info))
            bid_response = cpc.make_bid(
                ads_info=ads_info,
                bid_request_info=bid_request,
                ctr_info=ctr_info)
            log.info("bid response {}".format(bid_response))
            print(bid_request, type(bid_request), bid_request.dict())
        if bid_response["price"] < bid_request.dict()["bid_floor"]:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return bid_response
    except Exception as e:
        log.error("Make bid error: {}".format(e))



if __name__ == "__main__":
    uvicorn.run(app=app)
