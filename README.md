# Golden Raspberry Awards API

API RESTful desenvolvida em Python utilizando FastAPI para leitura e processamento de dados de filmes indicados e vencedores do Golden Raspberry Awards (Pior Filme).

---

## Tecnologias

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Pytest

---

## Instalação

```bash
# Clone o projeto
git clone https://github.com/barretobsa1903/api-movies.git
cd golden-raspberry-api

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
uvicorn main:app --reload


