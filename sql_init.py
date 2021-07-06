from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Video(Base):
    __tablename__ = 'video'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    youtube_id = Column(String(250), nullable=False)
    thumb_url = Column(String(250), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'youtube_id': self.youtube_id,
            'thumb_url': self.thumb_url,
        }

class Match_result(Base):
    __tablename__ = 'match_result'

    id = Column(Integer, primary_key=True)
    json_path = Column(String(250), nullable=False)
    superchat_num = Column(Integer, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'json_path': self.json_path,
            'superchat_num': self.superchat_num
        }


engine = create_engine('sqlite:///videos.db')


Base.metadata.create_all(engine)