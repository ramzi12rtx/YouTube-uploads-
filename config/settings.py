import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    IMAGE_STYLE = "digital art"
    IMAGE_SIZE = "1024x1024"
