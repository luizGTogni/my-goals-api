# **MyGoals**
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/yuribodo/a-base-vem-forte/blob/main/LICENSE)

O **MyGoals** é uma solução voltada para o gerenciamento de objetivos pessoais e profissionais.
Os usuários podem criar objetivos e, dentro deles, definir tarefas que funcionam como etapas a serem cumpridas.

A cada tarefa concluída, o usuário avança no progresso do objetivo, tornando o processo mais motivador através da gamificação.

---

## Índice

- [**MyGoals**](#mygoals)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [**Backend**](#backend)
      - [**Funcionalidades Principais**](#funcionalidades-principais)
      - [**Tecnologias**](#tecnologias)
    - [**Testes**](#testes)
      - [**Abordagem de Testes**](#abordagem-de-testes)
      - [**Tecnologias Utilizadas para Testes**](#tecnologias-utilizadas-para-testes)
  - [Instalação](#instalação)
    - [**Pré-requisitos**](#pré-requisitos)
    - [**Passos**](#passos)
  - [Como contribuir](#como-contribuir)
  - [Contato](#contato)

---

## Introdução

No ambiente corporativo, muitas pessoas e equipes enfrentam dificuldades em definir, acompanhar e concluir seus objetivos. A falta de organização, o excesso de tarefas dispersas e a ausência de motivação contínua resultam em metas abandonadas ou mal executadas.

Esses desafios não apenas comprometem a produtividade e o foco, mas também geram frustração e perda de engajamento.

**GoalManager** foi criado para solucionar esse problema, oferecendo uma plataforma onde usuários podem estruturar seus objetivos em tarefas claras, acompanhando o progresso de forma visual e envolvente. A utilização de gamificação torna o processo mais motivador, transformando a conquista de metas em uma experiência dinâmica, divertida e recompensadora.

---

## Tecnologias Utilizadas

### **Backend**

#### **Funcionalidades Principais**

- **Registro de Usuário**: Cadastro de novos usuários.
- **Login de Usuário**: Autenticação segura (JWT) para acesso às funcionalidades.
- **Gerenciamento de Objetivos**: CRUD para gerenciar objetivos.
- **Gerenciamento de Tarefas**: CRUD para gerenciar tarefas específica do objetivo.

#### **Tecnologias**

- **Linguagem**: Python
- **Framework**: Flask
- **Docker**: Docker compose
- **Banco de Dados**: PostgreSQL (SQLAlchemy ORM)
- **Autenticação**: Baseada em token JWT

### **Testes**
#### **Abordagem de Testes**
Foram implementados **testes unitários** em toda a aplicação para garantir a qualidade e a robustez do sistema.
#### **Tecnologias Utilizadas para Testes**
- **pytest**: Utilizado para criar testes unitários.

---

## Instalação

### **Pré-requisitos**
Certifique-se de que você tenha instalado:
- `Python 3.8+`
- Docker

### **Passos**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/luizGTogni/api-goals-manager-python.git
    ```

2. **Navegue para o repositório:**:

   ```bash
   cd api-goals-manager-python
   ```

3. **Instale as dependências:**:

   - For Backend:

     ```bash
     cd Backend
     python -m venv venv # Cria o ambiente virtual
     source venv/bin/activate  # Linux/Mac # Acessa o ambiente virtual
     venv\Scripts\activate  # Windows # # Acessa o ambiente virtual
     pip install -r requirements.txt
     ```
    
4. Configure o banco de dados:
      - Edite o arquivo .env e rode 
      ```bash
      docker compose up -d
      ```
5. Suba as migrations:
    ```bash
    alembic upgrade head
    ```

- **Para executar o Backend**:
1. Certifique-se de que o ambiente virtual está ativado
2. Inicie o servidor Flask:
    ```bash
    python run.py
    ```
3. Acesse o backend no navegador em: http://localhost:3000
  

## Como contribuir
1. **Fork esse repositório.**
2. **Crie uma branch para a sua mudança:**
   ```bash
   git checkout -b sua-branch
   ```
3. **Faça suas alterações e envie um pull request:**
   ```bash
     git add .
     git commit -m "feat: Descrição da mudança"
     git push origin sua-branch
   ```
---

## Contato
- Developers: Luiz Togni
- LinkedIn:
- [Luiz Togni](https://www.linkedin.com/in/luizgustavotogni/)