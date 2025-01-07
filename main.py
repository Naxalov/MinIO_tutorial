import minio

import os
# Get the access key and secret key from the environment
access_key = os.getenv('MINIO_ACCESS_KEY')
secret_key = os.getenv('MINIO_SECRET_KEY')

client = minio.Minio(
    "play.minio.io:9000",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
 
)

# Get list of buckets
buckets = client.list_buckets()
# Print the amount of buckets
print(len(buckets))
