from dotenv import load_dotenv
import os

load_dotenv()

ALLOWED_HOSTS = "http://localhost:3000"
class Settings:
    database_hostname: str = os.getenv("DATABASE_HOSTNAME")
    database_port: int = os.getenv("DATABASE_PORT")
    database_name: str = os.getenv("DATABASE_NAME")
    database_username: str = os.getenv("DATABASE_USERNAME")
    database_password: str = os.getenv("DATABASE_PASSWORD")
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("ALGORITHM")
    access_token_expire_minutes: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    ALLOWED_HOSTS: list =ALLOWED_HOSTS.split(",")
    class Config:
        env_file = ".env"
settings = Settings()