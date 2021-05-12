# db-ctr

## create dataset by csv

1. table schema

```
CREATE TABLE ctr (
    ad_id integer NOT NULL,
    status boolean NOT NULL,
    bidding_cpc double precision,
    advertiser text,
    banner_style text,
    category text,
    height double precision,
    width double precision,
    item_price  double precision,
    layout_style text,
    hist_ctr double precision,
    hist_cvr double precision,
    was_click boolean
);
```

2. Load data from csv

```
COPY ctr(ad_id,status,bidding_cpc,advertiser,banner_style,category,height,width,item_price,layout_style,hist_ctr,hist_cvr,was_click)
FROM '/ctr_dataset.csv'
DELIMITER ','
CSV HEADER;
```

3. Dump data to gz file

```
pg_dump -U dsp -d dsp | gzip  > /ctr_dataset.gz
```

## Restore 

```
gunzip < /ctr_dataset.gz | psql -U dsp --dbname dsp
```

