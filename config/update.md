
*stop the django server first*

*stash local changes to avoid conflict*
```bash
git add --all && git stash
```

*pull changes from remote repo*
```bash
git pull origin master
```

*activate the virtual environment*
```bash
source .venv/bin/activate
```

*install required packages*
```bash
pip install -r requirements.txt

```
*be in same directory as manage.py file*
```bash
cd biography/
```

*makemigrations and migrate*
```bash
python manage.py makemigrations
python manage.py migrate
```

*restore local changes*
```bash
git stash apply
git stash drop
```

*collect static files*
```bash
python manage.py collectstatic
```

*start the django server*
*use the **-w** flag followed with number of workers like:*
```bash
gunicorn -w 16 biography.asgi:application -k uvicorn.workers.UvicornWorker
```

