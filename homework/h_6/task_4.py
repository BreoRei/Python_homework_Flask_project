from databases import Database
from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'sqlite:///task.sqlite'

db = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base = declarative_base()


class TaskIn(BaseModel):
    title: str = Field(title='Title', max_length=50)
    description: str = Field(title='Description', default=None)
    done: bool = Field(title='Done', default=False)


class TaskOut(TaskIn):
    id: int


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text, nullable=True)
    done = Column(Boolean, default=False)


@asynccontextmanager
async def loop(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

Base.metadata.create_all(bind=engine)
app = FastAPI(loop=loop, title='Блокнот задач')


@app.get('/tasks/', response_model=list[TaskOut])
async def index():
    tasks = select(Task)
    return await db.fetch_all(tasks)


@app.get('/tasks/{task_id}', response_model=TaskOut)
async def get_task(task_id: int):
    task = await db.fetch_one(select(Task).where(Task.id == task_id))
    return task


@app.post('/tasks/', response_model=TaskIn)
async def create_task(task: TaskIn):
    new_task = insert(Task).values(**task.model_dump())
    await db.execute(new_task)
    return {**task.model_dump()}


@app.put('/tasks/{task_id}', response_model=TaskOut)
async def update_task(task_id: int, task: TaskIn):
    task_update = (update(Task).where(Task.id == task_id).values(**task.model_dump()))
    await db.execute(task_update)
    return await db.fetch_one(select(Task).where(Task.id == task_id))


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    task_db = await db.fetch_one(select(Task).where(Task.id == task_id))
    task = TaskOut.model_validate(
        {
            'id': task_db.id,
            'title': task_db.title,
            'description': task_db.description,
            'done': task_db.done
        }
    )
    task_del = delete(Task).where(Task.id == task_id)
    await db.execute(task_del)
    return {'message': 'задача успешно удалена', 'task': task.model_dump()}
