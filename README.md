1 - Crie uma conta no heroku https://signup.heroku.com/

2 - Instale o `heroku cli` https://devcenter.heroku.com/articles/heroku-cli

3 - Crie um novo `APP`

3.1 - Instale as dependencias:
```
poetry add gunicorn
poetry add whitenoise
```

3.2 - Adicione os arquivos:
-  `.gitignore`
```
__pycache__
*.pyc
env/
db.sqlite3

```

e no `.dockerignore`

```
__pycache__
*.pyc
env/
db.sqlite3
```

4 - Adicione a seguinte variável de ambiente: 
```
$ heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a ebac-bookstore-api
```

5 - Adicione no `bookstore/settings.py`: 
```
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'limitless-atoll-51647.herokuapp.com']
```

6 - Execute o comando:
```
heroku stack:set container -a ebac-bookstore-api
```

6.1 - Conectando o git + heroku
```
heroku git:remote -a ebac-bookstore-api
```

7 - Adicione o arquivo `heroku.yml`:
```
build:
  docker:
    web: Dockerfile
run:
  web: gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT
```

8 - Faça o deploy:
```
git push heroku main:main
```

9 - Execute as migrações:
```
heroku run python manage.py migrate

```

Obs: Para visualizar os logs no heroku execute o comando:
```
heroku logs -t
```