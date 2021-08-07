# -*- coding: utf-8 -*-
import os
import sys
from typing import Optional, Union


class Config:
    version: str = os.environ.get("VERSION", "0.1.0")
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
    access_token: str = os.environ.get("ACCESS_TOKEN")
    client_secret: Optional[str] = os.environ.get("CLIENT_SECRET")
    prefix: Optional[str] = os.environ.get("BOT_PREFIX", "%")
    owner: Optional[str] = os.environ.get("OWNER_NICK")
    site_url: Optional[str] = os.environ.get("BOT_SITE_URL")
    ai_url: Optional[str] = os.environ.get("BOT_AI_URL")
    ai_key: Optional[str] = os.environ.get("BOT_AI_KEY")
    webhook_url: Optional[str] = os.environ.get("BOT_WEBHOOK_URL")
    host: Optional[str] = os.environ.get("HOST")
    port: Optional[str] = os.environ.get("PORT")


class ApiConfig:
    analytics_url: Optional[str] = os.environ.get("API_ANALYTICS_URL", "https://tracker.dashbot.io/track")
    analytics_key: Optional[str] = os.environ.get("API_ANALYTICS_KEY")
    bugsnag_key: Optional[str] = os.environ.get("API_BUGSNAG_KEY")
    color_url: Optional[str] = os.environ.get("API_COLOR_URL", "https://www.thecolorapi.com")
    crypto_url: Optional[str] = os.environ.get("API_CRYPTO_URL", "https://rest.coinapi.io/v1/exchangerate")
    crypto_key: Optional[str] = os.environ.get("API_CRYPTO_KEY")
    currency_url: Optional[str] = os.environ.get("API_CURRENCY_URL", "https://v6.exchangerate-api.com/v6")
    currency_key: Optional[str] = os.environ.get("API_CURRENCY_KEY")
    math_url: Optional[str] = os.environ.get("API_MATH_URL", "https://api.mathjs.org/v4")
    translate_url: Optional[str] = os.environ.get("API_TRANSLATE_URL")
    twitch_url: Optional[str] = os.environ.get("API_TWITCH_URL", "http://decapi.me/twitch")
    weather_key: Optional[str] = os.environ.get("API_WEATHER_KEY")


class ProdConfig(Config, ApiConfig):
    mode: str = "prod"
    database_url: str = os.environ.get("DATABASE_URL")
    redis_url: Optional[str] = os.environ.get("REDIS_URL")


class LocalConfig(Config, ApiConfig):
    mode: str = "local"
    if os.environ.get("DATABASE_URL"):
        database_url: str = os.environ["DATABASE_URL"]
    else:
        database_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        database_file: str = os.path.join(database_dir, "db.sqlite3")
        database_url: str = f"sqlite:///{database_file}"
    redis_url: Optional[str] = os.environ.get("REDIS_URL")


class TestConfig(Config, ApiConfig):
    mode: str = "test"
    database_url: str = "sqlite://:memory:"
    redis_url: None = None
    bugsnag_key: None = None


config_options: dict = {"prod": ProdConfig, "local": LocalConfig, "test": TestConfig}
config_mode: str = os.environ.get("CONFIG_MODE", "local")

try:
    config: Union[ProdConfig, LocalConfig, TestConfig] = config_options[config_mode]
except KeyError:
    sys.exit(f"[CRITICAL] Invalid <CONFIG_MODE>. Expected 'local', 'test' or 'prod', not '{config_mode}'.")
else:
    print(f"[INFO] Running with <CONFIG_MODE>='{config.mode}'")
