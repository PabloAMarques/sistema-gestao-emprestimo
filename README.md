# Sistema de Gestão de Propostas de Empréstimo Pessoal

Este é um sistema de gestão de propostas de empréstimo pessoal desenvolvido utilizando Django, Django Rest Framework, Django Celery e RabbitMQ.

O sistema permite que os usuários cadastrem propostas de empréstimo pessoal, preencham os campos necessários e recebam uma avaliação de aprovação ou negação da proposta. As propostas são enviadas para uma fila RabbitMQ, onde o Django Celery processa as tarefas de avaliação e atualiza o status da proposta no banco de dados.

## Configuração do Ambiente

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina antes de prosseguir.

1. Clone o repositório do projeto:

```bash
git clone <link do repositorio>
cd sistema-gestao-propostas-emprestimo
```

2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```plaintext
SECRET_KEY=seu_secret_key_aqui
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest
```

3. Execute o seguinte comando para iniciar o ambiente Docker:

```bash
docker-compose up -d --build
```

4. Acesse o container do Django para executar os comandos adicionais:

```bash
docker-compose exec web bash
```

5. Dentro do container, execute os seguintes comandos para configurar o projeto:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Siga as instruções para criar um usuário administrador.

6. Acesse o admin do Django em seu navegador:

```
http://localhost:8000/admin/
```

Faça login com as credenciais do usuário administrador para acessar a interface de administração.

7. Para encerrar o ambiente Docker, execute o seguinte comando:

```bash
docker-compose down
```

## Utilização do Sistema

### Página de Preenchimento da Proposta

Acesse a página de preenchimento da proposta em seu navegador:

```
http://localhost:8000/propostas/
```

Preencha todos os campos solicitados e envie a proposta. Após o envio, a proposta será processada em segundo plano e o status será atualizado no banco de dados.

### Administração do Sistema

Acesse o admin do Django em seu navegador:

```
http://localhost:8000/admin/
```

Faça login com as credenciais do usuário administrador.

- Propostas: Nesta seção, você pode visualizar todas as propostas cadastradas juntamente com seus respectivos status. Você pode filtrar e pesquisar propostas conforme necessário.

## Estrutura do Projeto

- docker-compose.yaml: Arquivo de configuração do Docker Compose para definir os serviços e ambientes.
- Dockerfile: Arquivo de construção da imagem Docker para o projeto Django.
- web: Diretório do projeto Django.
  - settings.py: Arquivo de configuração principal do Django.
  - urls.py: Arquivo de definição de rotas do Django.
  - propostas: Aplicativo Django para gerenciar empréstimos.

