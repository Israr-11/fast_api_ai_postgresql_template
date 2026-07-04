from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_", env_file=".env", extra="ignore")

    user: str = "postgres"
    password: str  # required — no default, pydantic will raise if missing
    host: str = "localhost"
    port: str = "5432"
    name: str = "name"

    @property
    def uri(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class GeminiConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="GEMINI_", env_file=".env", extra="ignore")

    api_key: str


class DashguardConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DASHGUARD_", env_file=".env", extra="ignore")

    url: str
    api_key: str
    client_key: str


class VectorDBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="VECTOR_DB_", env_file=".env", extra="ignore")

    url: str
    api_key: str


class Settings(BaseSettings):
    """Root settings object — central access point for all app config."""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    gemini: GeminiConfig = Field(default_factory=GeminiConfig)
    dashguard: DashguardConfig = Field(default_factory=DashguardConfig)
    vector_db: VectorDBConfig = Field(default_factory=VectorDBConfig)


@lru_cache
def get_settings() -> Settings:
    """Cached singleton — Settings is built once per process, not once per import."""
    return Settings()