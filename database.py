from sqlalchemy import create_engine

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from model import *

BASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    url=BASE_URL, pool_pre_ping=True, echo=True)
BaseModel.metadata.create_all(engine)  # noqa: F405
