#!/bin/bash
set -e
gunzip < /ctr_dataset.gz |psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" 