TAG = 0.1.0
db-ctr-build:
	docker build -f ./src/db/ctr/dockerfile -t dsp/db-ctr:${TAG} .

db-ctr-up:
	docker run -it -d \
        -p 5432:5432 \
		--rm \
	    --name db-ctr \
	    dsp/db-ctr:${TAG}

db-ctr-exec:
	docker exec -it db-ctr psql -U dsp dsp

ml-storage-build:
	docker build -f ./src/ml/storage/dockerfile -t dsp/ml-storage:${TAG} .

ml-storage-up:
	docker run -it -d\
        -p 9000:9000 \
		--rm \
	    --name ml-storage \
	    dsp/ml-storage:${TAG}  server /data


db-ads-build:
	docker build -f ./src/db/ads/dockerfile -t dsp/db-ads:${TAG} .

db-ads-up:
	docker run -it -d \
        -p 5433:5432 \
		--rm \
	    --name db-ads \
	    dsp/db-ads:${TAG}

db-ads-exec:
	docker exec -it db-ads psql -U dsp dsp_rtb
