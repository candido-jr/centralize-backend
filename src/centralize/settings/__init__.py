from split_settings.tools import include
from dotenv import load_dotenv

load_dotenv()

base_settings = [
    "components/common.py",
    "components/database.py",
    "components/cache.py",
    "components/libs.py",
]

include(*base_settings)
