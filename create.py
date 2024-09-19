from flask import Flask,request,Blueprint, render_template
from Database.database import Usuario,Chaves
app = Blueprint('Create',__name__)

@app.route("/",methods=['GET'])

# Cria a pagina create 
def create():
    nome = request.args.get('nome')
    key_api = request.args.get('key')
    data_nascimento = request.args.get('dob')
    nome_da_mae = request.args.get('mae')
    cpf = request.args.get('cpf')
    email = request.args.get('email')
    senha = request.args.get('senha')

# Verifica os valores informados 
    data = verificar_valores([data_nascimento,nome_da_mae,cpf,email,senha,nome])
    valida_api = verificar_chave_api(key_api)

# verifica os dados e a api 
    if data and valida_api and verificar_user_existente(cpf,email) == 'nao':
            Usuario.create(nome=nome,data_de_nascimento=data_nascimento,nome_da_mae=nome_da_mae,cpf=cpf,email=email,senha=senha,saldo=0)
            return 'deu'

    elif valida_api is None:
#   retorna paginas de erro 
        return render_template('Erros_pagina_create/chave_api_invalida.html')
    elif verificar_user_existente(cpf,email) == 'existe':
        return 'aa'
    else:
        return render_template('Erros_pagina_create/campos_vazios_invalidos.html')
    
# verifica e trata os valores recebidos
def verificar_valores(valores : list):
    for valor in valores:
        if valor == None or not valor:
            return False
        elif len(valor) < 3:
            return False
    return True

# consulta e verifica as chaves api 
def verificar_chave_api(key : str):
    try:
        Chaves.select().where(Chaves.key == key).get()
        return True
    except:
        return None

# verifica se o cpf e o email estao cadastrados 

def verificar_user_existente(cpf,email):
    try:
        Usuario.select().where(Usuario.cpf == cpf).get()
        Usuario.select().where(Usuario.email == email).get()
        return f'existe'
    except Exception as e :
        return 'nao'
