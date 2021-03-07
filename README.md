# Carrinho de Compras

Carrinho de compras é um sistema de e-commerce, nossa API tem como objetivo realizar as operações necessárias para um site de vendas online, como por exemplo aplicar desconto, filtrar lista de produtos, etc.


Esse app exige a versão 3 do Python.

### Preparação

Crie um arquivo `.env` com as variáveis de acordo com o seu ambiente

```console
$ cat .env
APP_PORT=5000
DEBUG=True
```

Em `requirements.txt` é detalhado as dependências e as respectivas versões que são exigidas e que podem ser instaladas usando:

`$ pip install -r requirements.txt`

### Execução

Na raiz do projeto execute:

`python run.py`

# Estórias de Usuário

### AUTENTICAÇÃO

Narrativa:
Como um usuário 
Eu quero me autenticar no sistema
Para ser autenticado e poder fazer minha compra

Login:
Dado que eu digito meu login e minha senha correta e cliquei no botão fazer login, então o sistema verifica minhas credenciais e sou redirecionado para a página de compras.

### ADICIONAR/REMOVER/EDITAR ITENS AO CARRINHO

Narrativa:
Como um usuário autenticado no sistema
Eu quero adicionar itens ao carrinho
Para posteriormente realizar a compra

Adicionar itens:
Através de uma lista de produtos disponíveis, eu clico nos produtos que quero adicionar ao carrinho.

Editar Items: 
Dado que existem itens no carrinho, e desejo editar a quantidade de um determinado item, então eu posso clicar no botão ‘+’ ou ‘-’ referente ao respectivo item que desejo editar.

Remover items:
Dado que existem itens no carrinho e eu desejo removê-los, diminuo a quantidade desejada, clicando no botão ‘-’, até zerá-la e então o item é retirado do carrinho.


### FILTROS

Narrativa:
Como um usuário autenticado no sistema
Eu quero adicionar filtrar os itens
Para procurar mais fácil o item que desejo adicionar ao carrinho

A-Z:
Dado que eu cliquei no filtro A-Z, então o sistema exibe os itens de forma alfabeticamente ordenados.

Menor Preço:
Dado que eu cliquei no filtro Menor Preço, então o sistema exibe os itens ordenados de acordo com o seu preço, nesse caso do menor para o maior.

Maior Preço:
Dado que eu cliquei no filtro Menor Preço, então o sistema exibe os itens ordenados de acordo com o seu preço, nesse caso do maior para o menor.

### ADICIONAR CUPOM DE DESCONTO

Narrativa:
Como um usuário autenticado no sistema
Eu quero adicionar um cupom de desconto a minha compra
Para realizar a compra

Cupom Frete:
Dado que eu digitei um código de cupom válido referente a frete grátis no campo (Código de Desconto), então será descontado do valor final da minha compra o valor do frete

Cupom Desconto Quantia:
Dado que eu digitei um código de cupom válido referente a uma quantia fixa no campo (Código de Desconto), então será descontado do valor final da minha compra o valor do cupom.
Cupom Desconto Porcentagem:
Dado que eu digitei um código de cupom válido referente a uma porcentagem no campo (Código de Desconto), então o valor final da minha compra será descontado equivalente aquela porcentagem.

### FINALIZAR COMPRAR
Narrativa:
Como um usuário autenticado no sistema
Eu quero finalizar minha compra
Para sair do sistema com sucesso

Finalizar compra:
Dado que eu adicionei todos os itens ao carrinho, usei o cupom de desconto e desejo finalizar minha compra, então eu clico no botão finalizar compra,e o sistema me mostra o código de barras a ser pago.
