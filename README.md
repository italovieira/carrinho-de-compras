# Carrinho de Compras

Carrinho de compras é um sistema de e-commerce, nossa API tem como objetivo realizar as operações necessárias para um site de vendas online, como por exemplo aplicar desconto, filtrar lista de produtos, etc.


Esse app exige a versão 3 do Python.

### Preparação

Crie um arquivo `.env` com as variáveis de acordo com o seu ambiente

```console
$ cat .env
APP_PORT=5000
DEBUG=True
MONGO_URI=mongodb://localhost:27015
MONGO_DATABASE=carrinho-de-compras
JAEGER_HOST=localhost
```

Em `requirements.txt` é detalhado as dependências e as respectivas versões que são exigidas e que podem ser instaladas usando:

`$ pip install -r requirements.txt`

### Execução

Na raiz do projeto execute:

`python run.py`

### Testes

Para executar os testes de integração da nossa aplicação:

`docker-compose run --rm app pytest`

# Estórias de Usuário

https://github.com/italovieira/carrinho-de-compras/wiki/Est%C3%B3rias-de-Usu%C3%A1rio


# Documentação da API

https://github.com/italovieira/carrinho-de-compras/wiki/API
