from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# this is the url of the database
DB_URL = "sqlite:///./no_fap.db"

engin = create_engine(DB_URL, connect_args={"check_same_thread": False}, echo=True)

# this is for all the models
Base = declarative_base()

# create session for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)



def get_db():
    """
    Dependency to get a database session.
    Yields a session object and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
