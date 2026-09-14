from dataclasses import dataclass


@dataclass
class Settings:
    upload_queue_url: str | None = None


settings = Settings()
