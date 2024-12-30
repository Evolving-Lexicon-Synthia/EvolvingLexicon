import numpy as np
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String, unique=True)
    vector = Column(String)  # Store vector as a string for simplicity
    svnn_t = Column(Float)
    svnn_i = Column(Float)
    svnn_f = Column(Float)

class LexiconManager:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_word(self, word, vector, svnn_t=1.0, svnn_i=0.0, svnn_f=0.0):
        vector_str = str(vector.tolist())
        word_entry = Word(word=word, vector=vector_str, svnn_t=svnn_t, svnn_i=svnn_i, svnn_f=svnn_f)
        self.session.add(word_entry)
        self.session.commit()

    def get_word_vector(self, word):
        word_entry = self.session.query(Word).filter_by(word=word).first()
        if word_entry:
            return np.array(eval(word_entry.vector))
        else:
            return None

    def update_word_vector(self, word, new_vector):
        word_entry = self.session.query(Word).filter_by(word=word).first()
        if word_entry:
            word_entry.vector = str(new_vector.tolist())
            self.session.commit()

    def update_word_svnn(self, word, svnn_t, svnn_i, svnn_f):
        word_entry = self.session.query(Word).filter_by(word=word).first()
        if word_entry:
            word_entry.svnn_t = svnn_t
            word_entry.svnn_i = svnn_i
            word_entry.svnn_f = svnn_f
            self.session.commit()
