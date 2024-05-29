import json
import requests
import boto3
import uuid
import random

dynomodb = boto3.resource("dynamodb")
table = dynomodb.Table("PokemonDatabase")

def lambda_handler(event, context):
    unique_id = str(uuid.uuid4())
    # Get the Pokémon name from the event
    pokemon_name = event.get('queryStringParameters', {}).get('pokemon_name', 'ditto').lower()

    # Build the PokeAPI URL
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    # Send a request to the PokeAPI
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*', 
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }

    # Parse the response
    data = response.json()
    color_random = random.random()
    important_data = {
        'ID': unique_id,
        'name': data['name'],
        'abilities': [{'name': ability['ability']['name']} for ability in data['abilities']],
        'types': [{'name': type['type']['name']} for type in data['types']],
        'height': data['height'],
        'weight': data['weight'],
        'sprites': {
            'selected_sprite': data['sprites']['front_shiny'] if color_random < 0.2 else data['sprites']['front_default']
        }
    }
    print(color_random)

    table.put_item(Item=important_data)

    # Return the important data
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  
            'Content-Type': 'application/json'
        },
        'body': json.dumps(important_data)
    }