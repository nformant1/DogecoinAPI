import logging
from environs import Env

env = Env()
env.read_env()

# rpc
RPC_USER: str = env("RPC_USER")
RPC_PASSWORD: str = env("RPC_PASSWORD")
RPC_HOST: str = env("RPC_HOST")
RPC_PORT: int = env.int("RPC_PORT")  # type: ignore
# optional
ENV: str = env("ENV", "PROD")
LOG_LEVEL: str | int = env.log_level(  # type: ignore
    "LOG_LEVEL", logging.INFO)
# server
HOST: str = env("HOST", "0.0.0.0")
PORT: int = env.int("PORT", 443)  # type: ignore
SSL_KEYFILE: str = env("SSL_KEYFILE", None)
SSL_CERTFILE: str = env("SSL_CERTFILE", None)
