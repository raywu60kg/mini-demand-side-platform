from pydantic import BaseModel
import os

default_ctr = os.getenv("default_ctr", )

minio_server_info = {
    "uri": os.getenv("minio_uri", "localhost:9000"),
    "access_key": os.getenv("minio_access_key", "dsp"),
    "secret_key": os.getenv("secret_key", "00000000")
}

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


class ModelInput(BaseModel):
    ad_id: str
    status: bool
    bidding_cpc: float
    advertiser: str
    banner_style: str
    category: str
    height: float
    width: float
    item_price: float
    layout_style: str
    hist_ctr: float
    hist_cvr: float


class ModelOutput(BaseModel):
    prediction: float

class HealthCheckOutput(BaseModel):
    health: bool
