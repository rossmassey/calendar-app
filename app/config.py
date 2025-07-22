from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROVIDER: str = "test"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "MedSpa Booking API"
    
    class Config:
        env_file = ".env"


settings = Settings() 