from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    category = Column(String)
    date_added = Column(DateTime, default=datetime.datetime.utcnow)
    date_completed = Column(DateTime)
    status = Column(Integer, default=1)  # 1 = active, 2 = completed
    position = Column(Integer, nullable=False)
