from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
print(f"Database Port: {settings.database_port}")  # Should print 2224
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")  # Should print postgresql://postgres:Shaina05@@localhost:2224/fastapi
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',port="2224", database='fastapi', user='postgres', password='Shaina05@', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database successfully connected")
#         break
#     except Exception as e:
#         print(e, "errror")
#         time.sleep(2)