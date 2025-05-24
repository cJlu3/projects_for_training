from database import engine, session_factory, Base
from sqlalchemy import text, insert
from models import WorkersOrm

def return_sql_version():
    with engine.connect() as conn:
        res = conn.execute(text("select version()"))
        print(f"{res=}")

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    

def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username = "Bobr")
        worker_volk = WorkersOrm(username = "Volk")
        session.add_all([worker_bobr, worker_volk])
        session.commit()
