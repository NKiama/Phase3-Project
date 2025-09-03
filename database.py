from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Todo
import datetime

engine = create_engine("sqlite:///todos.db")
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def insert_todo(task, category):
    session = SessionLocal()
    count = session.query(Todo).count()
    todo = Todo(
        task=task,
        category=category,
        position=count,
        status=1,
        date_added=datetime.datetime.now()
    )
    session.add(todo)
    session.commit()
    session.close()

def get_all_todos():
    session = SessionLocal()
    todos = session.query(Todo).order_by(Todo.position).all()
    session.close()
    return todos

def delete_todo(position):
    session = SessionLocal()
    todo = session.query(Todo).filter_by(position=position).first()
    if todo:
        session.delete(todo)
        session.commit()
        todos = session.query(Todo).order_by(Todo.position).all()
        for i, t in enumerate(todos):
            t.position = i
        session.commit()
    session.close()

def update_todo(position, task=None, category=None):
    session = SessionLocal()
    todo = session.query(Todo).filter_by(position=position).first()
    if todo:
        if task:
            todo.task = task
        if category:
            todo.category = category
        session.commit()
    session.close()

def complete_todo(position):
    session = SessionLocal()
    todo = session.query(Todo).filter_by(position=position).first()
    if todo:
        todo.status = 2
        todo.date_completed = datetime.datetime.now()
        session.commit()
    session.close()
