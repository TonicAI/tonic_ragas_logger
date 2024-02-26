import os
from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        load_dotenv()

        self.TONIC_VALIDATE_API_KEY = os.getenv(
            "TONIC_VALIDATE_API_KEY",
        )
        self.TONIC_VALIDATE_BASE_URL = os.getenv(
            "TONIC_VALIDATE_BASE_URL", "https://validate.tonic.ai/api/v1"
        )
