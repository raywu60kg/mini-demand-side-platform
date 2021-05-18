# mini-demand-side-platform
## Tech stack
- api: fastapi
- container: docker, docker-compose
- ml modeling: sklearn
- ml model serving: fastapi
- ml model storage: minio
- OLTP: postgres
- OLAP: postgres


## usage
1. Build images
```
docker-compose build
```

2. Activate services
```
docker-compose up
```

3. test with curl
```
curl -X 'POST' \
  'http://localhost:8000/bw_dsp' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "bid_floor": 0,
  "height": 0,
  "width": 0,
  "hist_ctr": 0,
  "hist_cvr": 0
}'
```

## future
- Enhance ml training fuction
- Load balance
- Monitoring
- OLTP HA
- MLOPS

## reference
- https://fastapi.tiangolo.com/deployment/docker/
- https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/