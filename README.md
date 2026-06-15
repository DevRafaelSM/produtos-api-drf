# API REST de Produtos com Django REST Framework

## Objetivo

Criar uma API REST para gerenciamento de produtos utilizando Django e Django REST Framework.

A aplicação permite cadastrar, listar, consultar, atualizar e inativar produtos por meio de requisições HTTP e respostas
no formato JSON.

## Tecnologias utilizadas

* Python;
* Django;
* Django REST Framework;
* Django REST Framework Spectacular;
* SQLite;
* Swagger/OpenAPI.

## Funcionalidades

* Cadastrar produtos;
* Listar todos os produtos;
* Consultar produto por ID;
* Atualizar todos os dados de um produto;
* Atualizar parcialmente um produto;
* Inativar produtos;
* Consultar produtos ativos e inativos;
* Gerar documentação OpenAPI;
* Testar os endpoints pela interface do Swagger.

## Estrutura do produto

Cada produto possui os seguintes campos:

* **id:** identificador único gerado automaticamente;
* **nome:** nome obrigatório do produto, com até 100 caracteres;
* **descricao:** descrição opcional, com até 1000 caracteres;
* **preco:** valor decimal obrigatório, maior ou igual a `0.01`;
* **ativo:** indica se o produto está ativo, com valor padrão `true`;
* **criado_em:** data e hora da criação, preenchidas automaticamente;
* **atualizado_em:** data e hora da última atualização, preenchidas automaticamente.

## Como executar

### 1. Criar o ambiente virtual

```bash
py -m venv .venv
```

### 2. Ativar o ambiente virtual

```bash
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Aplicar as migrations

```bash
python manage.py migrate
```

### 5. Executar o servidor

```bash
python manage.py runserver
```

A aplicação ficará disponível, por padrão, em:

```text
http://127.0.0.1:8000/
```

## Endpoints

### Listar produtos

```http
GET /api/produtos/
```

Retorna todos os produtos cadastrados, incluindo produtos ativos e inativos.

### Cadastrar produto

```http
POST /api/produtos/
```

Exemplo de requisição:

```json
{
  "nome": "Teclado",
  "descricao": "Teclado com switches azuis",
  "preco": "150.00",
  "ativo": true
}
```

O campo `ativo` é opcional. Caso não seja enviado, o produto será criado como ativo.

### Consultar produto por ID

```http
GET /api/produtos/{id}/
```

Retorna os dados do produto correspondente ao ID informado.

Caso o produto não exista, a API retorna uma resposta HTTP `404`.

### Atualizar produto completamente

```http
PUT /api/produtos/{id}/
```

Atualiza todos os campos editáveis do produto.

Os campos obrigatórios devem ser enviados na requisição.

### Atualizar produto parcialmente

```http
PATCH /api/produtos/{id}/
```

Permite alterar somente os campos enviados.

Exemplo:

```json
{
  "preco": "175.00"
}
```

### Inativar produto

```http
DELETE /api/produtos/{id}/
```

O produto não é excluído fisicamente do banco de dados.

O endpoint realiza uma exclusão lógica, alterando o campo:

```text
ativo = false
```

Produtos inativos continuam disponíveis nas consultas da API.

Caso o produto já esteja inativo, a API retorna uma resposta informando que a operação não pode ser realizada novamente.

## Regras de validação

### Nome

* É obrigatório;
* Não pode ser vazio;
* Não pode conter apenas espaços;
* Deve possuir no máximo 100 caracteres.

### Descrição

* É opcional;
* Deve possuir no máximo 1000 caracteres.

### Preço

* É obrigatório;
* Deve ser um valor decimal válido;
* Deve ser maior ou igual a `0.01`;
* Não aceita valores iguais a zero ou negativos.

### Ativo

* Deve ser um valor booleano;
* Caso não seja informado no cadastro, assume o valor `true`.

### Campos protegidos

Os seguintes campos são controlados pela aplicação e não podem ser alterados diretamente pelo usuário:

* `id`;
* `criado_em`;
* `atualizado_em`.

## Documentação da API

### Swagger

A documentação interativa pode ser acessada em:

```text
http://127.0.0.1:8000/api/docs/
```

Por meio do Swagger, é possível visualizar e testar os endpoints da API.

### Schema OpenAPI

O schema da API pode ser acessado em:

```text
http://127.0.0.1:8000/api/schema/
```

## Migrations

Após qualquer alteração no arquivo `produtos/models.py`, gere uma nova migration:

```bash
python manage.py makemigrations
```

Depois, aplique as alterações no banco de dados:

```bash
python manage.py migrate
```

## Dependências

Para atualizar o arquivo `requirements.txt` com as dependências instaladas no ambiente virtual, execute:

```bash
python -m pip freeze > requirements.txt
```

## Observações gerais

* O projeto utiliza Views Genéricas do Django REST Framework;
* A listagem e o cadastro utilizam `ListCreateAPIView`;
* A consulta, atualização e inativação utilizam `RetrieveUpdateDestroyAPIView`;
* O método `DELETE` realiza inativação lógica;
* O projeto utiliza SQLite como banco de dados local;
* O arquivo `db.sqlite3` não é versionado;
* A API foi testada manualmente utilizando requisições GET, POST, PUT, PATCH e DELETE;
* A documentação OpenAPI é gerada com `drf-spectacular`.
