from flask import Flask,request,Blueprint, jsonify,render_template
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
        
        return retornar_json({'Error':'Nao autorizado',
         'Message':'Chave Api Invalida',
         'status code': 403},403)
    elif verificar_user_existente(cpf,email) == 'existe':
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

def verificar_user_existente(cpf,email):
    try:
        Usuario.select().where(Usuario.cpf == cpf).get()
        Usuario.select().where(Usuario.email == email).get()
        return f'existe'
    except Exception as e :
        return 'nao'

def retornar_json(data,code):
    return jsonify(data), code