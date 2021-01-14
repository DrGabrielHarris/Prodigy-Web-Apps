from sqlalchemy import create_engine, text

user = "user name"
password = "user password"
host = "host name"
port = 3306

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}",
    connect_args={"ssl": {"ssl_ca": "certificate.crt.pem"}},
)

with engine.connect() as cnxn:
    cnxn.execute(text("""CREATE DATABASE IF NOT EXISTS prodigydb;"""))
