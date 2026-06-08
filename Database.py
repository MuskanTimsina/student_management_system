from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
DATABASE_URL="postgresql://postgres:muskan123@localhost:5432/school_db"
engine=create_engine(DATABASE_URL)

sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()



