# 📝 Docker Flask Backend + Docker Nginx Frontend

Projeto de semente que separa **backend Flask** e **frontend estático** (apenas com javascript) em contêineres distintos usando **Docker Compose**.  

## 📚 Sumário

- [Arquitetura](#arquitetura)
- [Pré-requisitos](#pré-requisitos)
- [Como rodar](#como-rodar)
- [Workflow de desenvolvimento](#workflow-de-desenvolvimento)
- [Endpoints da API](#endpoints-da-api)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Próximos passos](#próximos-passos)

---

## Arquitetura

| Serviço   | Porta local | Função                               |
|-----------|-------------|--------------------------------------|
| **backend** (Flask) | 5000 | API REST `/api/todos` com CORS e *auto-reload* |
| **frontend** (Nginx) | 3000 | Servidor de arquivos estáticos (HTML + CSS + JS) |

A comunicação é feita via HTTP; o frontend chama a API Flask em `http://backend:5000` (Docker bridge) ou `http://localhost:5000` fora dos contêineres.

---

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/) 20.10+  
- [Docker Compose](https://docs.docker.com/compose/) (já incluído no Docker Desktop)

---

## Como rodar

```bash

# constrói as imagens e sobe os contêineres
docker compose up --build
