## Pagina de Documentacao da API
![image](https://github.com/user-attachments/assets/c6fe231e-d507-4244-9cfa-0ab8ddd42895)

## Descricao 
Esta API CRUD foi desenvolvida utilizando Python com o framework Flask. O banco de dados utilizado é o MySQL, e foi implementada criptografia com Salt para proteger as senhas e assegurar a segurança dos dados. Todas as respostas da API são fornecidas no formato JSON.


## Funcionalidades
## **Create**
Esta funcionalidade permite adicionar novos usuários à base de dados. Abaixo estao algumas funcionalidades da pagina CREATE
- Verifica os argumentos passados e verifica a veracidade dos dados
- Valida a chave APi
- Verifica se o Usuario com os dados passados ja existe no banco de dados
- A senha e enviada para a DB criptografada com uma chave segura
- Todos os parametros sao enviados pela URL

Mensagens retornadas : 
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
Esta funcionalidade permite Excluir um Usuario do banco de dados pelo id informado. Os argumentos inseridos sao verificados, e verificado se o id e um numero valido e verifica tambem se o usuario existe antes de ser excluido 
valida e verifica a chave API e nao aceita caracteres especiais (% ' * ^ ) como argumento 
