import minio

import os
# Get the access key and secret key from the environment
access_key = os.getenv('MINIO_ACCESS_KEY')
secret_key = os.getenv('MINIO_SECRET_KEY')

print(f'acc_key: "{access_key}" secret key "{secret_key}"')
# Initialize the client
client = minio.Minio(
    "cdn.qarshidu.uz:9001", # Only the host name and port
    access_key=access_key,
    secret_key=secret_key,
    secure=False
)


