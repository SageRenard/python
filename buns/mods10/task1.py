import requests
import json

def get_starship_info(ship_id=10):

    data = json.loads(requests.get(f'https://swapi.dev/api/starships/{ship_id}').text)

    pilots = []

    for pilot_url in data['pilots']:
    
        pilot_info_all = json.loads(requests.get(pilot_url).text)

        homeworld_url = pilot_info_all['homeworld']
        homeworld_info = json.loads(requests.get(homeworld_url).text)

        pilot_info = {
            'name': pilot_info_all['name'],
            'height': pilot_info_all['height'],
            'mass': pilot_info_all['mass'],
            'homeworld': homeworld_info['name'],
            'homeworld_url': homeworld_url
        }

        pilots.append(pilot_info)

    new_data = {
        'name': data['name'],
        'max_atmosphering_speed': data['max_atmosphering_speed'],
        'starship_class': data['starship_class'],
        'pilots': pilots
    }

    return new_data

if __name__ == "__main__":
    starship_info = get_starship_info()

    with open('info_starship.json', 'w') as file:
        json.dump(starship_info, file, indent=4)

    print(json.dumps(starship_info, indent=4))
