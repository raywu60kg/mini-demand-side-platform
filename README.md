# mini-demand-side-platform
![image](pictures/infra.png)

check the infra on web [here](https://www.plectica.com/maps/EBS5LQRHZ)
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

## service
- bidding-server docs: localhost:8000/docs
- ml-training docs: localhost:8001/docs
- ml-serving docs: localhost:8002/docs
- minio: localhost:9000
  - access_key: dsp
  - secret_key: 00000000
  
## future
- Enhance ml training function
- Load balance
- Monitoring
- OLTP HA
- MLOPS

## reference
- https://fastapi.tiangolo.com/deployment/docker/
- https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/