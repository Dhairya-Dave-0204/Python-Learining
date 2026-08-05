from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.utils.settings import settings

Base = declarative_base()

engine = create_engine(url= settings.DB_CONNECTION)

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