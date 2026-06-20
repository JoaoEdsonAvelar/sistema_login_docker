# Sistema de Cadastro e Login - Infraestrutura com Docker, Nginx e MySQL

Este projeto simula uma infraestrutura moderna de microsserviços isolados e orquestrados, desenvolvida como requisito avaliativo para a disciplina de **Segurança de Redes / Infraestrutura de Sistemas**.

A aplicação consiste em um sistema completo de cadastro e autenticação de usuários, utilizando um Proxy Reverso para controle de borda, uma API Backend em Flask e persistência de dados isolada em MySQL.

## 🏗️ Arquitetura do Ecossistema

O ambiente é composto por 3 containers principais interconectados de forma segura através da rede virtual interna `sistema_login_default`:

1. **Nginx (`sistema_login_nginx`):** Proxy reverso operando na porta pública `8080` (ou `80`), interceptando requisições do cliente e encaminhando-as de forma segura para o backend.
2. **Flask API (`sistema_login_app`):** Backend em Python 3.10 gerenciado via servidor WSGI Gunicorn na porta interna `5000`. Implementa hashing criptográfico de senhas via `bcrypt`.
3. **MySQL (`sistema_login_db`):** Banco de dados relacional operando de forma isolada na porta `3306`, inacessível externamente ao host.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de possuir instalado em sua máquina:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Git

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/sistema_login_docker.git](https://github.com/SEU_USUARIO/sistema_login_docker.git)
cd sistema_login_docker/sistema_login

#Verificar o status dos containers ativos:
docker-compose ps

#Monitorar logs em tempo real da API Flask (Diagnóstico de Erros):
docker logs -f sistema_login_app

#Derrubar e limpar o ambiente virtual:
docker-compose down