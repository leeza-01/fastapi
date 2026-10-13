from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
database_url = "mysql+pymysql://root:cfg1234@localhost/learning_tracker"
engine =  create_engine(database_url)

SessionLocal = sessionmaker(
    autocommit=False,
     autoflush=False,
      bind=engine
      )

Base = declarative_base()
