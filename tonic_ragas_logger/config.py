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
        self.TONIC_VALIDATE_TELEMETRY_URL = os.getenv(
            "TONIC_VALIDATE_TELEMETRY_URL", "https://telemetry.tonic.ai/validate"
        )
        self.TONIC_RAGAS_DO_NOT_TRACK = os.getenv(
            "TONIC_RAGAS_DO_NOT_TRACK", "false"
        ).lower() in ("true", "1", "t")