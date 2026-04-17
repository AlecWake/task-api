from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:awake2390@localhost:5432/taskdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine)