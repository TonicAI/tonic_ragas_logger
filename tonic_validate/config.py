import os
from dotenv import load_dotenv

load_dotenv()

TONIC_VALIDATE_API_KEY = os.getenv(
    "TONIC_VALIDATE_API_KEY",
)
TONIC_VALIDATE_BASE_URL = os.getenv(
    "TONIC_VALIDATE_BASE_URL", "https://validate.tonic.ai/api/v1"
)
