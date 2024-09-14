from peewee import *

db = MySQLDatabase('mysql://root:admin@127.0.0.1:3306/Banco_de_Dados')

class Molde_da_db(Model):
    nome = CharField()
    data_de_nascimento = DateField()
    nome_da_mae = CharField()
    cpf = IntegerField()
    email = CharField()
    senha = TextField()
    class Meta:
        database = db


