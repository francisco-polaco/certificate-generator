from os import PathLike

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DataSourceConfig(BaseModel):
    path: PathLike
    sheet: str

    class Config:
        frozen = True
        extra = "forbid"


class SourcesConfig(BaseModel):
    data: DataSourceConfig
    template: PathLike

    class Config:
        frozen = True
        extra = "forbid"


class Settings(BaseSettings):
    sources: SourcesConfig
    output_dir: PathLike

    class Config:
        frozen = True
        extra = "forbid"


config = Settings()


def get_config():
    return config
