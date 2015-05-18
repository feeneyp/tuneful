import os.path

from flask import url_for
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from tuneful import app
from database import Base, engine

class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    
    def as_dictionary(self):
        song = {
            "id": self.id,
            "song": { "id": self.file_id,
                "name": self.file.name }
        }
        return song    
    
class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    name = Column(String(128)) #name = Column(String(128), unique=True)
    song = relationship("Song", backref="file", uselist=False)

      
    def as_dictionary(self):
      return {
          "id": self.id,
          "name": self.name,
          "path": url_for("uploaded_file", filename=self.name)
      }
                  

