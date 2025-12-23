---
# ⚙️ Resume Analyzer – Backend (FastAPI)

Backend desenvolvido em **FastAPI** responsável por realizar a **análise inteligente de currículos em PDF**.
A API recebe o arquivo enviado pelo frontend, processa o conteúdo e retorna uma análise estruturada com **compatibilidade com a vaga**, **pontos fortes** e **pontos de melhoria**.

Este projeto foi construído com foco em **arquitetura de APIs REST**, **boas práticas**, **separação de responsabilidades** e **facilidade de integração com frontends web e mobile**.

---

## 🚀 Funcionalidades

* 📥 Recebimento de currículos em **PDF**
* 📄 Processamento e extração de texto do currículo
* 🧠 Análise do conteúdo do currículo
* 📊 Geração de resultado estruturado:

  * Score de compatibilidade
  * Pontos fortes
  * Pontos a melhorar
* 🔗 Endpoints REST documentados automaticamente
* ⚠️ Tratamento de erros e validações
* 🌐 Pronto para integração com Flutter, React ou outros frontends

---

## 🧠 Tecnologias Utilizadas

* **Python**
* **FastAPI**
* **Uvicorn**
* **Pydantic** (validação de dados)
* **Python-Multipart** (upload de arquivos)
* **PDF Parsing** (extração de texto)
* **CORS Middleware**

---

## 🔌 Endpoints Principais

### 📤 Enviar currículo para análise

```http
POST /analysis/upload
```

**Descrição:**
Recebe um arquivo PDF e inicia o processo de análise.

**Parâmetros:**

* `file` (multipart/form-data) – currículo em PDF

**Resposta:**

```json
{
  "analysis_id": "string"
}
```

---

### 📊 Obter resultado da análise

```http
GET /analysis/{analysis_id}
```

**Descrição:**
Retorna o resultado completo da análise do currículo.

**Resposta:**

```json
{
  "score": 85,
  "strengths": [
    "Boa experiência com backend",
    "Conhecimento em APIs REST"
  ],
  "weaknesses": [
    "Pouca experiência com cloud",
    "Ausência de projetos open source"
  ]
}
```

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* Python 3.10+
* Virtualenv (opcional, recomendado)

### Passos

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Entrar na pasta
cd seu-repositorio

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
uvicorn app.main:app --reload
```

---

## 📘 Documentação Interativa

Após iniciar o servidor, acesse:

* **Swagger UI:**
  `http://localhost:8000/docs`

* **ReDoc:**
  `http://localhost:8000/redoc`

Essas interfaces permitem testar os endpoints diretamente pelo navegador.

---

## 🔐 CORS

A API possui **CORS configurado**, permitindo consumo por aplicações frontend hospedadas em outros domínios, como Flutter Web ou React.

---

## 📌 Objetivo do Projeto

* Demonstrar domínio de **FastAPI**
* Criação de APIs REST escaláveis
* Organização de código e arquitetura limpa
* Processamento de arquivos no backend
* Projeto realista para **portfólio profissional**

---

## 👨‍💻 Autor

**Paulo Carneiro** </br>
Estudante de Ciência da Computação </br>
Desenvolvedor Full Stack </br>

---
