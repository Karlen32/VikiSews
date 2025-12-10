from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
NEW_PASSWORD = os.getenv("NEW_PASSWORD")
REPEAT_PASSWORD = os.getenv("REPEAT_PASSWORD")

