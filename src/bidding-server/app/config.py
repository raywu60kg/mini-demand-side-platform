from pydantic import BaseModel
import os

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
class RequestInput(BaseModel):
    bidfloor: float
    height: float
    weight: float
    hist_ctr: float
    hist_cvr: float

class RequestOutput(BaseModel):
    price: float
    ad_id: str
