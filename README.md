## Pagina de Documentacao da API
![image](https://github.com/user-attachments/assets/c6fe231e-d507-4244-9cfa-0ab8ddd42895)

## Descricao 
Esta e uma API CRUD desenvolvida em python em conjunto com a biblioteca Flask, utilizei tambem o banco de dados MySql
e uma criptografia do tipo Salt para manter a seguranca dos dados, todas as respostas da API sao em json 

## Funcionalidades
-**Create**
Esta funcao permite ao usuario da api adicionar usuarios,ela criptografa a senha com uma criptografia com chave privada e envia os dados para o banco de dados e insere os usuarios no Banco de Dados MySql
todos os argumentos sao passados pela url, A API ira retornar mensagens de sucesso e erro, a API verifica se os caracteres passados como argumento sao validos, se o usuario existe no banco de dados e se a chave api
informada e valida, deixarei abaixo as resposas da API 

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
