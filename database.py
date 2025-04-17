from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.models import Base

DATABASE_URL = "sqlite:///test.db"

engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)