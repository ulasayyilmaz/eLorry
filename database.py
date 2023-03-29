from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv(ENGINEKEY, default=None), 
connect_args={
    "ssl": {
        "ca": os.getenv(ENGINECONFIG, default=None),
    }
})


def create_put_requestdb():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE put_request(CompanyName VARCHAR);"))

def put_request():
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO requests (CompanyName) VALUES ('CHEP');"))
        result = conn.execute(text("SELECT * FROM requests"))
        row = result.all()
        if len(row) == 0:
            return None
        else:
            return row[0]._mapping