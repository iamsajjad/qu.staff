
# Biography
Biography is web based platform for creating, saving and updating personal biography.

**Run Biography Server**

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

*for local development run*
```bash
python manage.py runserver --settings=biography.local
```

*start gunicorn*
```bash
gunicorn biography.asgi:application -k uvicorn.workers.UvicornWorker
```

*use the **-w** flag followed with number of workers like:*
```bash
gunicorn -w 2 biography.asgi:application -k uvicorn.workers.UvicornWorker
```

*edit and configure the Caddyfile*
```bash
nvim Caddyfile
```

*running caddy to handle users requests*
```bash
sudo caddy run --config Caddyfile
```

