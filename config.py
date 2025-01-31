import os
from os import PathLike
from typing import Any

import yaml
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


class YamlConfigSettingsSource(PydanticBaseSettingsSource):
    def get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]:
        # Method not used in this class as the entire .yml file is loaded directly, but still forced to be implemented
        # https://github.com/pydantic/pydantic-settings/issues/102
        return None, field_name, False

    def __call__(self) -> dict[str, Any]:
        config_file = "config.yml"

        if not os.path.exists(config_file):
            raise FileNotFoundError("The configuration file '{}' does not exist.".format(config_file))

        model = {}
        with open(config_file) as f:
            model.update(yaml.safe_load(f))

        return model


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


class OutputConfig(BaseModel):
    path: PathLike
    columns_to_filename: list[str]

    class Config:
        frozen = True
        extra = "forbid"


class Settings(BaseSettings):
    sources: SourcesConfig
    output: OutputConfig

    @classmethod
    def settings_customise_sources(cls,
                                   settings_cls: type[BaseSettings],
                                   init_settings: PydanticBaseSettingsSource,
                                   env_settings: PydanticBaseSettingsSource,
                                   dotenv_settings: PydanticBaseSettingsSource,
                                   file_secret_settings: PydanticBaseSettingsSource) -> tuple[
        PydanticBaseSettingsSource, ...]:
        # Add load from yml file, change priority and remove file secret option
        # https://docs.pydantic.dev/latest/concepts/pydantic_settings/#adding-sources
        return env_settings, YamlConfigSettingsSource(settings_cls), init_settings, file_secret_settings

    class Config:
        frozen = True
        extra = "forbid"


config = Settings()


def get_config():
    return config
