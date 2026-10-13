from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
database_url = "mysql+pymysql://root:cfg1234@localhost/FASTAPI"
engine =  create_engine(database_url)

SessionLocal = sessionmaker(
    autocommit=False,
     autoflush=False,
      bind=engine
      )

Base = declarative_base()
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()