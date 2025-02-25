import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
if response.status_code == 200:
    print(response.json())