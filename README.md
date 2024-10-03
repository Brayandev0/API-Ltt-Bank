## Pagina de Documentacao da API
![image](https://github.com/user-attachments/assets/c6fe231e-d507-4244-9cfa-0ab8ddd42895)

## Descricao 
Esta API CRUD foi desenvolvida utilizando Python com o framework Flask. O banco de dados utilizado é o MySQL, e foi implementada criptografia com Salt para proteger as senhas e assegurar a segurança dos dados. Todas as respostas da API são fornecidas no formato JSON.
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

Mensagens de Resposta desta parte da API.

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


Mensagens de Resposta desta parte da API.

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
  "Message": "O Usuario com o id 1 nao existe ",
  "status code": 400
}
```
** Sucesso**
```{
  "Message": "O Usuario com o id 9 foi excluido com sucesso",
  "Success": "Sua requisicao foi aceita",
  "status code": 200
}
```
