## Pagina de Documentacao da API
![image](https://github.com/user-attachments/assets/c6fe231e-d507-4244-9cfa-0ab8ddd42895)

## Descricao 
Esta API CRUD foi desenvolvida utilizando Python com o framework Flask. O banco de dados utilizado é o MySQL, e foi implementada criptografia com Salt para proteger as senhas e assegurar a segurança dos dados. Todas as respostas da API são fornecidas no formato JSON, A API esta operando na porta 5000 e Foi desenvolvida para um banco ficticio 
## Tecnologias Usadas
- Banco de dados MySql
- biblioteca de criptografia Bcrypt e uma chave privada salva na db
- Biblioteca peewee
- Framework flask
- Biblioteca Jsonify para respostas em JSON

## Funcionalidades

## **Create**
Esta funcionalidade permite adicionar novos usuários à base de dados. Abaixo estao algumas funcionalidades da parte /create
- Verifica os argumentos passados e verifica a veracidade dos dados
- Retorna Todas as respostas em JSON
- Valida a chave APi
- Verifica se o Usuario com os dados passados ja existe no banco de dados
- A senha e enviada para a DB criptografada com uma chave segura
- Todos os parametros sao enviados pela URL

Respostas da API.


**Chave API invalida***
```{
  "Error": "Nao autorizado",
  "Message": "Chave Api Invalida",
  "status code": 403
}
```
**Argumentos invalidos**
```{
  "Error": "Campos invalidos",
  "Message": "Os argumentos passados estao invalidos ou incorretos",
  "status code": 403
}
```
**Usuario ja existe no Banco de dados**
```{
  "Error": "Usuario ja existe",
  "Message": "O usuario ja existe no banco de dados",
  "status code": 403
}
```
**Sucesso**
```{
  "Message": "Usuario inserido e criado com sucesso",
  "Success": "Conta criada com sucesso",
  "status code": 200
}
```
## Delete
Esta funcionalidade permite Excluir um Usuario do banco de dados pelo id informado. Abaixo estao algumas funcionalidades da parte /delete
- O id e verificado se e um numero valido
- A chave API e verificada antes de realizar a funcionalidade
- Bloqueia caracteres especiais para evitar vulnerabilidades de injecao de codigo
- Verifica se o id realmente existe na db antes de excluir 

Respostas da API.


**Argumentos invalidos**
```{
  "Erro": "Os parametros nao foram passados corretamente ",
  "Message": "Argumentos invalidos ou nulos foram inseridos",
  "status code": 403
}
```
** Chave API invalida***
```{
  "Error": "Sua chave api nao foi aceita",
  "Message": "A chave api inserida e invalida",
  "status code": 403
}
```
** Usuario inexistente***
```{
  "Error": "O id informado e invalido",
  "Message": "O Usuario com o id { id informado} nao existe ",
  "status code": 400
}
```
** Sucesso**
```{
  "Message": "O Usuario com o id { id informado } foi excluido com sucesso",
  "Success": "Sua requisicao foi aceita",
  "status code": 200
}
```
## Update
Esta funcionalidade permite voce mudar os dados do Usuario pelo id,e passar como argumento na url apenas os campos que voce quer alterar. Abaixo estarao algumas funcionalidades desta parte /update
- Verifica a veracidade dos argumentos passados
- Verifica se o id passado e valido
- Verifica se o Usuario existe no banco de dados
- Verifica a chave API informada
- Verifica e protege o programa verificando os argumentos passados contra injecao de codigo malicioso
- Retorna em JSON

Respostas da API.


**Argumentos invalidos**
```
  "Error':"Argumentos invalidos",
  "Message": "Os argumentos inseridos sao invalido, revise e tente novamente",
  "status code": 403
```
**Id invalido**
```
  'Error':'Id invalido',
  'Message': 'O id informado e invalido ou nao existe na db',
  'status code': 400
```
**Chave API invalida**
```
  'Error':'Chave API invalida',
  'Message': 'A chave API inserida e invalida ',
  'status code': 403
```
**Sucesso**
```
 'Success':'O Usuario foi modificado',
 'Message': 'O Usuario Foi modificado com sucesso',
  'status code': 200
```

## Read 
Esta funcionalidade permite ter acesso aos dados do Usuario pelo id, ela fornece o nome completo, nome da mae, email, cpf, data de nascimento,se a conta esta ativa no banco e fornece o saldo atual. Abaixo estao as principais funcionalidades 
- Verifica se a chave API e valida
- Verifica se o id inserido existe na db e se e realmente um numero
- Verifica se o usuario existe antes da consulta
- Retorna Respostas em  JSON

Respostas da API.


**Id invalido**
```
{
  "Error": "ID invalido",
  "Message": "id inserido nao existe ou e invalido,",
  "status code": 400
}
```
**Chave API invalida**
```
{
  "atividade da conta": "ativa",
  "cpf": "123736123",
  "data_nascimento": "11112006",
  "email": "vieirabrayan42@gmail.com",
  "nome": "Administrador",
  "nome da mae": "Ryana beonce",
  "saldo R$": 0
}
```
(Todos os dados acima sao ficticios e nao pertencem a ninguem, apenas o email e verdadeiro)
