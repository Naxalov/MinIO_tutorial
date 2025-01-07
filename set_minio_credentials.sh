#!/bin/bash


# Assign the first argument to PATH_TO_JSON
PATH_TO_JSON="$1"

# Extract accessKey and secretKey using jq
ACCESS_KEY=$(jq -r '.accessKey' "$PATH_TO_JSON")
SECRET_KEY=$(jq -r '.secretKey' "$PATH_TO_JSON")

# Export the variables
export MINIO_ACCESS_KEY="$ACCESS_KEY"
export MINIO_SECRET_KEY="$SECRET_KEY"

echo "MINIO_ACCESS_KEY: $MINIO_ACCESS_KEY"
echo "MINIO_SECRET_KEY: $MINIO_SECRET_KEY"

