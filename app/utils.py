import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(key: str) -> str:
    """Safely get environment variable value."""
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Missing environment variable: {key}")
    return value
