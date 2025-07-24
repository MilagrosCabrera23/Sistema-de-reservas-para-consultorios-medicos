from sqlalchemy.orm import sessionmaker
from app.core.database.connection import engine

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()