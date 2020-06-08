from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQL Alchemy ORM engine to interact with Docker PostgreSQL database
engine = create_engine('postgresql://usr:pass@localhost:5432/news_scanner')
Session = sessionmaker(bind=engine)

# Base class for class definitions
Base = declarative_base()
