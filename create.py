from flask import Flask,request,Blueprint, jsonify
from Database.database import Usuario,Chaves, Salt
import bcrypt


create_ = Blueprint('Create',__name__)

@create_.route("/",methods=['GET'])

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
    if data and valida_api and verificar_user_existente(cpf,email):
            Usuario.create(nome=nome,data_de_nascimento=data_nascimento,nome_da_mae=nome_da_mae,cpf=cpf,email=email,senha=criptografar_Salt(senha),saldo=0,atividade='ativa')
            return retornar_json({'Success':'Conta criada com sucesso',
                                  'Message':'Usuario inserido e criado com sucesso',
                                  'status code':200},200)

    elif valida_api is None:
#   retorna paginas de erro 
        
        return retornar_json({'Error':'Nao autorizado',
         'Message':'Chave Api Invalida',
         'status code': 403},403)
    elif not verificar_user_existente(cpf,email):
        return retornar_json({'Error':'Usuario ja existe',
                              'Message':'O usuario ja existe no banco de dados',
                              'status code': 403},403)
    else:
        return retornar_json({'Error':'Campos invalidos',
                              'Message':'Os argumentos passados estao invalidos ou incorretos',
                              'status code': 403},403)
    
# verifica e trata os valores recebidos
def verificar_valores(valores : list):
    for valor in valores:
        if valor in ['?','%','*','^']:
            return False
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

# verifica se o cpf e o email estao cadastrados na db 

def verificar_user_existente(cpf : str ,email : str):
    if Usuario.select().where((Usuario.cpf == cpf) | (Usuario.email == email)).exists():
        return False
    return True

# transforma os dados do tipo dicionario em jsonify
def retornar_json(data : dict,code : int):
    return jsonify(data), code

# criptografa a senha com Salt
def criptografar_Salt(texto : str):
    salt_da_db : str = Salt.get_by_id(1)
    return bcrypt.hashpw(texto.encode('utf-8'),salt_da_db.chave.encode('utf-8')).decode('utf-8')

