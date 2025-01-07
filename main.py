import minio

import os
# Get the access key and secret key from the environment
access_key = os.getenv('MINIO_ACCESS_KEY')
secret_key = os.getenv('MINIO_SECRET_KEY')

print(f'Access Key: {access_key} Secret Key {secret_key}')