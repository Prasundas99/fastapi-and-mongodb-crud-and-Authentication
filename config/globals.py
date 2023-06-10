from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = os.environ.get("DB_URI")
DB_NAME = os.environ.get("DB_NAME")


