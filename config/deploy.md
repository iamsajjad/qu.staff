
*create virtual environment*
```bash
python -m venv .venv
```

*activate the virtual environment*
```bash
source .venv/bin/activate
```

*install required packages*
```bash
pip install -r requirements.txt
```

*create postgresql database with user and password*
```bash
sudo -u postgres psql
```
```sql
CREATE ROLE biouser WITH LOGIN PASSWORD 'w1G01z6dX3PvZYISi';
CREATE DATABASE biographydb WITH OWNER biouser ENCODING 'utf-8';
GRANT ALL PRIVILEGES ON DATABASE biographydb to biouser;
ALTER USER biouser CREATEDB;
```
*be in same directory as manage.py file*
```bash
cd biography/
```

*makemigrations and migrate*
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

*create super user*
```bash
python manage.py createsuperuser
```

*use the **-w** flag followed with number of workers like:*
```bash
gunicorn -w 16 biography.asgi:application -k uvicorn.workers.UvicornWorker
```

