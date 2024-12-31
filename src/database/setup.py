from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

db_url = "postgresql://postgres:Scrde.ca7476@localhost/evolving_lexicon_db"
Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String, unique=True)
    vector = Column(String)
    svnn_t = Column(Float)
    svnn_i = Column(Float)
    svnn_f = Column(Float)

class Context(Base):
    __tablename__ = 'contexts'
    id = Column(Integer, primary_key=True)
    context_id = Column(String, unique=True)
    description = Column(String)

class WordContext(Base):
    __tablename__ = 'word_contexts'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    context_id = Column(String)
    vector = Column(String)
    svnn_t = Column(Float)
    svnn_i = Column(Float)
    svnn_f = Column(Float)

def setup_database():
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    setup_database()
