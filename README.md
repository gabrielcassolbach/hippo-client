-- Passo 1: criar um .venv
python -m venv .venv

-- Passo 2: entrar no .venv
source .venv/bin/activate

-- Passo 3: instalar todas dependências do projeto
pip install -r requirements.txt

-- Passo 4: toda vez que instalar uma dependência (primeiramente, entre no .venv)
pip freeze > .requirements.txt
