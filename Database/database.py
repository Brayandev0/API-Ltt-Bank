import peewee 
from peewee import CharField,TextField,IntegerField,DateField, Model
db = peewee.MySQLDatabase(
    'Banco_de_Dados',
    user='root',
    password='admin',
    host='127.0.0.1',
    port=3306
)

db.connect()

class Usuario(Model):
    nome = CharField(27)
    data_de_nascimento = CharField(10)
    nome_da_mae = CharField(20)
    cpf = CharField(15)
    email = CharField(26)
    senha = TextField()
    saldo = IntegerField()
    class Meta:
        database = db

class Chaves(Model):
    nome = CharField(30)
    key = TextField(220)
    class Meta:
        database = db
db.create_tables([Usuario])

db.create_tables([Chaves])

