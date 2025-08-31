import minio
from dotenv import load_dotenv
import os
# Get the access key and secret key from the environment
# Load environment variables from .env file
load_dotenv()
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

client = minio.Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Upload a file
file_path = "/Users/naxalov/github/codeschool/MinIO_tutorial/README.md"
bucket_name = "my-bucket2"
object_name = "file.md"

client.fput_object(bucket_name, object_name, file_path)