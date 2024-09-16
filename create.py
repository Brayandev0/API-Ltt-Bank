from flask import Flask,request,Blueprint, render_template
import http

from Database.database import Usuario
app = Blueprint('Create',__name__)

@app.route("/")
def create():
    nome = request.args.get('nome')
    key_api = request.args.get('key')
    data_nascimento = request.args.get('dob')
    nome_da_mae = request.args.get('mae')
    cpf = request.args.get('cpf')
    email = request.args.get('email')
    senha = request.args.get('senha')
    valores = [data_nascimento,nome_da_mae,cpf,email,senha,nome]
    data = verificar_valores(valores,key_api)

    if data and tratar_valores(valores,cpf):
        Usuario.create(nome=nome,data_de_nascimento=data_nascimento,nome_da_mae=nome_da_mae,cpf=cpf,email=email,senha=senha)
        return 'deu'
    elif data == None:
        return render_template('Erros_pagina_create/chave_api_invalida.html')
    else:
        return render_template('Erros_pagina_create/campos_vazios_invalidos.html')
    
def verificar_valores(valores : list, key : str):
    for valor in valores:
        if valor == None or not valor:
            return False
    try:
        if int(key) in [0,934,43,12,12]:
            return True
    except:
        return None
    else:
        return None
 
def tratar_valores(lista : list, cpf : str):
    for valor in lista:
        if len(valor) < 3:
            return False
        try:
            int(cpf) + 3
        except :
            return False
        return True
