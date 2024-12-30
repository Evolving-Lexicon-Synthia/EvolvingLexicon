from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost/evolving_lexicon_db" #Change for you need

def get_engine():
    return create_engine(DATABASE_URL)

def create_tables(engine):
    Base.metadata.create_all(engine)
