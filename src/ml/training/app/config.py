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

