from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROVIDER: str = "test"
    
    class Config:
        env_file = ".env"


settings = Settings() 