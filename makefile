TAG = 0.1.0
db-ctr-build:
	docker build -f ./src/db/ctr/dockerfile -t dsp/db-ctr:${TAG} .

db-ctr-up:
	docker run -d \
        -p 5432:5432 \
		--rm \
	    --name db-ctr \
	    dsp/db-ctr:${TAG}

db-ctr-exec:
	docker exec -it db-ctr psql -U dsp