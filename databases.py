from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base() 	 
	
'''#class User(base):
  	 _tablename_="user'spoems"
  	 id = Column(int )
  	 name = Column(str)
  	 text = Column(str)
  	 user_id =Column(Integer , Primary_key=true)
  	 background = Column(str)
'''
class Poem (Base):
       __tablename__="poem"
       id = Column(Integer, primary_key=True )
       name = Column(String)
       text = Column(String)
       bioofwriter = Column(String())
       background = Column(String())
       user_id = Column(Integer, ForeignKey('user.id'))
       user = relationship("User", back_populates="poems")
       topic = Column(String())
       #topic= relationship("Topic", back_populates="poems") 
       #topic_id = Column(Integer, ForeignKey('topics.id'))


class Quote(Base):
       __tablename__="quote"
       id = Column(Integer, primary_key=True)
       text = Column(String())
       background_image = Column(String())
       user_id = Column(Integer, ForeignKey('user.id'))
       user = relationship("User", back_populates="quotes")
       topic = Column(String())
       #topic= relationship("Topic", back_populates="quotes")
       #topic_id = Column(Integer, ForeignKey('topics.id'))
   	

# class Topic(Base):
#       __tablename__="topics"
#       id =Column(Integer , primary_key = True)
#       name = Column(String)
#       poems= relationship("Poem", back_populates="topic")  
#       quotes= relationship("Quote", back_populates="topic") 


class User(Base):
       __tablename__ = 'user'
       id = Column(Integer, primary_key=True)
       name = Column(String(255))
       email = Column(String(255), unique=True)
       password_hash = Column(String(255))
       quotes = relationship("Quote", back_populates="user")
       poems = relationship("Poem", back_populates="user")

       def hash_password(self, password):
              self.password_hash = pwd_context.encrypt(password)

       def verify_password(self, password):
              return pwd_context.verify(password, self.password_hash)


