import requests

# URL do endpoint que você quer acessar
url = "http://127.0.0.1:8000/api/profile/"

# Token de acesso que você recebeu do endpoint /api/token/
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1OTg5MDcyLCJpYXQiOjE3NTU5ODU0NzIsImp0aSI6Ijc5Y2QyZDViYzQzNDQzYmNhYmU4YjYyYzBjODgxZTRiIiwidXNlcl9pZCI6IjIifQ.SPYH5do5azrWG2t5lmFdE6-i8JVZGjb1hqCGZxG3i3M"
}

# Fazendo a requisição GET
response = requests.get(url, headers=headers)

# Mostrando o resultado
print(response.json())
