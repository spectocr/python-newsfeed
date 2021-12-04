from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  
  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete') #same thing as line below.
  votes = relationship('Vote', cascade='all,delete') #The Post model includes a dynamic property for votes, meaning that a query for a post should also return information about the number of votes the post has. We also want to make sure that when we delete a post from the database, every vote associated is subsequently deleted.

  vote_count = column_property(
  select([func.count(Vote.id)]).where(Vote.post_id == id)
  )