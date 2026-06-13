# Todo List API

Projeto de estudo desenvolvido durante o curso [Python do Zero ao Avancado com FastAPI](https://www.udemy.com/course/python-do-zero-ao-avancado-com-fastapi/), da Udemy.

Esta API representa uma lista de tarefas simples criada com FastAPI. O objetivo do projeto e praticar os fundamentos de desenvolvimento backend com Python, construindo endpoints HTTP de forma organizada e evolutiva.

## Por que fazer este curso

O curso ajuda a transformar conhecimento basico de Python em pratica aplicada ao desenvolvimento de APIs modernas. Ele e uma boa escolha para quem quer entender como estruturar projetos backend, criar rotas, receber dados por requisicoes e trabalhar com ferramentas comuns do ecossistema Python.

Ao acompanhar o curso e construir projetos como este, a pessoa pratica conceitos importantes em vez de apenas estudar teoria.

## O que voce ira aprender

- Criar uma API com FastAPI.
- Organizar rotas em arquivos separados.
- Criar endpoints para listar, cadastrar, concluir e deletar tarefas.
- Receber dados no corpo da requisicao usando modelos com Pydantic.
- Executar uma aplicacao localmente com Uvicorn.
- Testar endpoints HTTP durante o desenvolvimento.
- Evoluir um projeto Python de forma incremental.

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn
- uv

## Como executar

Instale as dependencias:

```bash
uv sync
```

Inicie o servidor de desenvolvimento:

```bash
make dev
```

A API ficara disponivel em:

```text
http://localhost:8000
```

## Endpoints atuais

- `GET /health` - verifica se a API esta respondendo.
- `GET /tasks` - lista as tarefas.
- `POST /tasks` - cria uma nova tarefa.
- `PATCH /tasks/{task_id}/done` - marca uma tarefa como concluida.
- `DELETE /tasks/{task_id}` - remove uma tarefa.

## Observacao

Este repositorio faz parte do meu processo de aprendizado. O codigo pode evoluir conforme eu avancar no curso e praticar novos conceitos.
