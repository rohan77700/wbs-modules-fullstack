import requests

while True:
    pokemon_name = input("Enter the name of a Pokémon: ")

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print("--- Pokemon Character ---")
        print(f"Name: {pokemon_data['name'].capitalize()}")
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(f"- {ability['ability']['name']}")
        print(f"Base Experience: {pokemon_data['base_experience']}")
        print("Types:")
        for pokemon_type in pokemon_data['types']:
            print(f"- {pokemon_type['type']['name']}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}")
    else:
        print("Invaild! Failed to fetch pokemon.")

    search = input("Do you want to find another pokemon? (yes/no): ").lower()
    if search != 'yes':
        break 