from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from os import getenv
load_dotenv()

Base = declarative_base()

# Model for users
class User(Base):
    __tablename__ = "user_auth"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

# Database config
DATABASE_URL = getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
localsession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create table
Base.metadata.create_all(bind=engine)