from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:GO74giPA84@localhost:5432/menu"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)

Base = declarative_base()