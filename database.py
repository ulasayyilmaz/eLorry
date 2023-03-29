from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

engine_key = os.environ['ENGINEKEY']
#engine_config = os.environ['ENGINECONFIG']

engine = create_engine(engine_key, 
connect_args={
    "ssl": {
        "ca": "/etc/ssl/cert.pem",
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
            return row[0]