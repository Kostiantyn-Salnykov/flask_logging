import functools
import logging
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MainSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file="example.env", env_file_encoding="utf-8")

    DEBUG: bool = Field(default=False)
    LOG_LEVEL: int = Field(default=logging.WARNING)
    LOG_STYLE: Literal["{", "%", "$"] = Field(default="{")
    LOG_FORMAT: str = Field(default="{asctime} - {levelname} - {message}")
    LOG_DATE_TIME_FORMAT: str = Field(default="%Y-%m-%dT%H:%M:%SZ")
    LOG_PATH: Path = Field(default="logs")


@functools.lru_cache()
def init_settings() -> MainSettings:
    return MainSettings()


Settings = init_settings()
