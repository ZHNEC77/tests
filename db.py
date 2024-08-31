import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


load_dotenv()
CONNECTION_ROW = os.getenv("CONNECTION_ROW")

Model = declarative_base(name="Model")

engine = create_engine(
    CONNECTION_ROW
)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


session = Session()
