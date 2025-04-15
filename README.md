# Dentro da pasta backend(se existir)
cd backend

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

# Navegar até a pasta backend (se necessário)
cd backend

# Instalar o CLI do Tailwind CSS globalmente (se ainda não tiver)
npm install -g npm
npm install -g @tailwindcss/cli

# Executar o Tailwind CSS em modo watch
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch

# em outro terminal
# Iniciar o servidor
python manage.py runserver