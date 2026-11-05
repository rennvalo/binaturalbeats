import os
import reflex as rx
from dotenv import load_dotenv

# Load environment variable from /data/.env if present, otherwise local data/.env
env_file = "/data/.env" if os.path.exists("/data/.env") else os.path.join(os.path.dirname(__file__), "data", ".env")
if os.path.exists(env_file):
    load_dotenv(env_file)

db_url = os.getenv("DATABASE_URL", "sqlite:////data/app.db")

config = rx.Config(
    app_name="binaturalbeats",
    db_url=db_url,
    env_file=env_file if os.path.exists(env_file) else None,
    telemetry_enabled=False,
)
