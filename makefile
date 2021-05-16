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
	docker exec -it db-ctr psql -U dsp

ml-storage-build:
	docker build -f ./src/ml/storage/dockerfile -t dsp/ml-storage:${TAG} .

ml-storage-up:
	docker run -it -d\
        -p 9000:9000 \
		--rm \
	    --name ml-storage \
	    dsp/ml-storage:${TAG}  server /data
