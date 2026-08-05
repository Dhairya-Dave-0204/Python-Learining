# By default the sql alchemy creates a pool of 5 connections when the create engine function is called
# one can explicitly define the pool attributes like follows for more personalizations

# Sqlalchemy is lazy so it only processes the connection when a query (read / write) is to be executed

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.utils.settings import settings

Base = declarative_base()

engine = create_engine(
    url=settings.DB_CONNECTION,
    pool_size=10,         # Keep up to 10 connections open and ready
    max_overflow=20,      # If the pool is full, allow up to 20 extra temporary connections
    pool_timeout=30,      # If no connections are available, wait 30 seconds before throwing an error
    pool_recycle=1800     # Reconnect connections older than 30 minutes to prevent database timeouts
)

Local_Session = sessionmaker(bind = engine)

def get_db():
    session = Local_Session()
    try:
        yield session
    except:
        print("Error in connecting to the DB")
        # return { "status": False, "message": "Error in getting the DB session" }
    finally:
        session.close()