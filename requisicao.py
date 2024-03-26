import json
import requests

def personagens():

    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

    response = requests.get(api_url)

    print(json.dumps(response.json(), indent=4))

personagens()