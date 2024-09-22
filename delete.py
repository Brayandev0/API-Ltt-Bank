from flask import Flask,Blueprint, jsonify, request
from Database.database import Chaves, Usuario

delete = Blueprint('/delete',__name__)

@delete.route('/')

# pagina principal 
def pagina_delete():
    api = request.args.get('key')
    id_user = request.args.get('id')
    api_verificada = verificar_chave_api(api) 

    if not api or not id_user:
        return Transformar_em_jsonify({
            'Erro':'Os parametros nao foram passados corretamente ',
            'Message':'Argumentos invalidos ou nulos foram inseridos',
            'status code': 403
            },403)
# verifica e retorna a mensagem de sucesso 
    if verificar_valor_do_id(id_user) and api_verificada:
            
            # verifica se o usuario existe antes de excluir 
            if verificar_se_o_usuario_exist(id_user):
                Usuario.delete_by_id(id_user)
                return Transformar_em_jsonify({
                    'Success':'Sua requisicao foi aceita',
                    'Message':f'O Usuario com o id {id_user} foi excluido com sucesso',
                    'status code': 200
                    },200)
            else:
                return Transformar_em_jsonify({
            'Error':'O id informado e invalido',
            'Message':f'O Usuario com o id {id_user} nao existe ',
            'status code': 400
            },400)
# Verifica se a api e invalida 
    elif api_verificada == None:
        return Transformar_em_jsonify({
            'Error':'Sua chave api nao foi aceita',
            'Message':'A chave api inserida e invalida',
            'status code': 403
            },403)
    
# verifica a chave api informada com consulta na db 
def verificar_chave_api(key : str):
    try:
        Chaves.get(Chaves.key == key)
        return True
    except:
        return None

# verifica se o id informado e realmente um numero 
def verificar_valor_do_id(id : str):
    if not id:
        return False
    try:
        int(id)
        return True
    except TypeError:
        return False
    
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