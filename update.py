from flask import Blueprint, Flask, request,jsonify
from Database.database import Usuario, Chaves
update_page = Blueprint("Update",__name__)

@update_page.route('/')
def home():
    nome = request.args.get('nome')
    id = request.args.get('id')
    key_api = request.args.get('key')
    data_nascimento = request.args.get('dob')
    nome_da_mae = request.args.get('mae')
    email = request.args.get('email')

# pega os valores para testarmos posteriormente
    verificacao_id = verificar_se_o_id_e_valido(id)
    verificacao_api_key = verificar_chave_api(key_api)

# verifica tudo e inicia a aplicacao 
    if  verificacao_id and verificacao_api_key:
        # verifica se  os valores sao validos
        if verificar_valores({'data de nascimento':data_nascimento,'nome da mae':nome_da_mae,'email':email,'nome':nome}):
            realizar_update({'data de nascimento':data_nascimento,'nome da mae':nome_da_mae,'email':email,'nome':nome},id)
            return Transformar_em_jsonify({'Success':'O Usuario foi modificado',
                                       'Message': 'O Usuario Foi modificado com sucesso',
                                       'status code': 200},200)   
        else:
            return Transformar_em_jsonify({'Error':'Argumentos invalidos',
                                       'Message': 'Os argumentos inseridos sao invalido, revise e tente novamente',
                                       'status code': 403},403)

    elif not verificacao_id:
        return Transformar_em_jsonify({'Error':'Id invalido',
                                       'Message': 'O id informado e invalido ou nao existe na db',
                                       'status code': 400},400)
    elif not verificacao_api_key:
        return Transformar_em_jsonify({'Error':'Chave API invalida',
                                       'Message': 'A chave API inserida e invalida ',
                                       'status code': 403},403)        
   
# verifica os argumentos e identifica os campos 
def realizar_update(valores : dict, id_user : str):
    user = Usuario.get_by_id(id_user)

# verifica se os valores sao validos e se a caracteres invalidos
    if valores['data de nascimento']:
        user.data_de_nascimento = valores['data de nascimento']

    if valores['nome da mae'] :
        user.nome_da_mae = valores['nome da mae']

    if valores['email'] :
        user.email = valores['email']

    if valores['nome']:
        user.nome = valores['nome']

# salva no banco de dados e retorna 
    user.save()
    return True

#verifica se o valor que informado e valido 

def verificar_valores(valor):
    for i in valor:
        if valor[i]:
            if len(valor[i]) <= 4:
                return False
            if valor[i] in ['?','%','*','^']:
                return False
            if i == 'nome' or i == 'email':
                try:
                    int(valor[i]) + 3
                    return False
                except ValueError:
                    return True
    return True

# verifica a api key 
def verificar_chave_api(key : str):
    try:
        Chaves.get(Chaves.key == key)
        return True
    except:
        return None
    


# verifica se o id existe na db e se e valido
def verificar_se_o_id_e_valido(id : str):
    try:
        Usuario.get_by_id(id)
        int(id)
        return True
    except:
        return False


# converte dicionarios nem jsonify
def Transformar_em_jsonify(data: dict, code: int):
    return jsonify(data), code
