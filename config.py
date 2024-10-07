from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Clothing Segmentation API"
    PROJECT_VERSION: str = "1.0.0"
    MODEL_NAME: str = "mattmdjaga/segformer_b2_clothes"
    MAX_IMAGE_SIZE: tuple = (620, 620)
    STATIC_DIR: str = "static"
    PROCESSED_DIR: str = f"{STATIC_DIR}/processed_images"
    BATCH_DIR: str = f"{PROCESSED_DIR}/batch_proccessed"

    class Config:
        env_file= ".env"
    
settings = Settings()