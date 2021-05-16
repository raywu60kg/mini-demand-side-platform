import os
train_method = os.getenv("train_method", "sklearn")
data_pipeline_method = os.getenv("data_pipeline_method", "postgres")
model_saver_method = os.getenv("model_saver_method", "minio")
postgres_server_info = {
    "host": os.getenv("postgres_host", "localhost"),
    "dbname": os.getenv("postgres_dbname", "dsp"),
    "user": os.getenv("postgres_user", "dsp"),
    "password": os.getenv("postgres_password", "dsp"),
    "host": os.getenv("postgres_host", "localhost"),
    "port": os.getenv("postgres_port", "5432")
}
minio_server_info = {
    "uri": os.getenv("minio_uri", "localhost:9000"),
    "access_key": os.getenv("minio_access_key", "dsp"),
    "secret_key": os.getenv("secret_key", "00000000")
}

data_columns = [
    "ad_id",
    "status",
    "bidding_cpc",
    "advertiser",
    "banner_style",
    "category",
    "height",
    "width",
    "item_price",
    "layout_style",
    "hist_ctr",
    "hist_cvr",
    "was_click"
]
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

target_features = "was_click"
