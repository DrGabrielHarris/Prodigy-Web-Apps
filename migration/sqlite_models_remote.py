from peewee import *

database = MySQLDatabase(
    user="user name",
    password="user password",
    host="host name",
    port=3306,
    database="database name",
    ssl={"ssl": {"ssl_ca": "certificate.crt.pem"}},
)


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class Dataset(BaseModel):
    created = IntegerField()
    meta = BlobField()
    name = CharField(unique=True)
    session = IntegerField()

    class Meta:
        table_name = "dataset"


class Example(BaseModel):
    content = BlobField()
    input_hash = IntegerField()
    task_hash = IntegerField()

    class Meta:
        table_name = "example"


class Link(BaseModel):
    dataset = ForeignKeyField(column_name="dataset_id", field="id", model=Dataset)
    example = ForeignKeyField(column_name="example_id", field="id", model=Example)

    class Meta:
        table_name = "link"


database.create_tables([Dataset, Example, Link])
# database.get_tables()
database.close()
