from pydantic import BaseModel
import os

feature_mapping = {
    0: {"layout_style": "AB"},
    1: {"layout_style": "RU"},
    2: {"layout_style": "GY"},
    3: {"layout_style": "MR"},
    4: {"layout_style": "BK"},
    5: {"layout_style": "BX"},
    6: {"layout_style": "RZ"},
    7: {"layout_style": "TY"},
    8: {"category": "Shirt"},
    9: {"layout_style": "DX"}
}


class RequestInput(BaseModel):
    bid_floor: float
    height: float
    width: float
    hist_ctr: float
    hist_cvr: float


class RequestOutput(BaseModel):
    price: float
    ad_id: int


class HealthCheckOutput(BaseModel):
    health: bool


bidding_strategy = os.getenv("bidding_strategy", "cpc")

get_ads_method = os.getenv("get_ads_method", "postgres")

postgres_server_info = {
    "host": os.getenv("postgres_host", "localhost"),
    "dbname": os.getenv("postgres_dbname", "dsp_rtb"),
    "user": os.getenv("postgres_user", "dsp"),
    "password": os.getenv("postgres_password", "dsp"),
    "host": os.getenv("postgres_host", "localhost"),
    "port": os.getenv("postgres_port", "5433")
}
model_uri = os.getenv("model_uri", "http://localhost:8000/model:predict")