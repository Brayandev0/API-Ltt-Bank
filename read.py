from flask import Blueprint,request ,jsonify
from Database.database import Chaves,Usuario
read = Blueprint("read",__name__)

@read.route('/')
def read_page():
    api_key = request.args.get("key")
    id = request.args.get("id")
    api_verificacao = verificar_chave_api(api_key)
    if verificar_valor_do_id(id) and api_verificacao and  verificar_se_o_usuario_exist(id) :
        a = Usuario.get_by_id(id)
        return f"{a.nome}"
    
    elif api_verificacao == None :
        return Transformar_em_jsonify({
            'Error':"A chave API inserida e invalida",
            "Message": "A chave api inserida e invalida, revise e tente novamente",
            "status code": 403
        },403)
    else:
        return Transformar_em_jsonify({
            "Error":"ID invalido",
            "Message": "id inserido nao existe ou e invalido,",
            "status code": 400}, 400)

def verificar_valor_do_id(id : str):
    if not id:
        return False
    try:
        int(id)
        return True
    except TypeError:
        return False
    
# verifica a chave api 
def verificar_chave_api(key : str):
    try:
        Chaves.get(Chaves.key == key)
        return True
    except:
        return None

# converte dicionarios nem jsonify
def Transformar_em_jsonify(data: dict, code: int):
    return jsonify(data), code

# verifica se o usuario existe na db 
def verificar_se_o_usuario_exist(data : str):
    try:
        Usuario.get_by_id(data)
        return True
    except:
        return False