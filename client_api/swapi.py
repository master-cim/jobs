
import requests

response = requests.get('https://swapi.dev/api/planets/1/')
diameter = response.json().get('diameter')
print(diameter)
