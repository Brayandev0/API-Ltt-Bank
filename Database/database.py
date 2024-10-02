import peewee # type: ignore
from peewee import CharField,TextField,IntegerField, Model

# realiza a conecao da db
db = peewee.MySQLDatabase(
    'Banco_de_Dados',
    user='root',
    password='admin',
    host='127.0.0.1',
    port=3306
)

db.connect()

# cria a tabela usuario
class Usuario(Model):
    nome = CharField(27)
    data_de_nascimento = CharField(10)
    nome_da_mae = CharField(20)
    cpf = CharField(15)
    email = CharField(26)
    senha = TextField()
    saldo = IntegerField()
    atividade = CharField(10)
    class Meta:
        database = db

# cria a tabela chaves 
class Chaves(Model):
    nome = CharField(30)
    key = TextField(220)
    class Meta:
        database = db
        
# cria a tabela salt 
class Salt(Model):
    chave = CharField(60)
    class Meta:
        database = db

# cria as tabelas  na db 
db.create_tables([Usuario])
db.create_tables([Salt])
db.create_tables([Chaves])

