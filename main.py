# api key: e6bcf177-33ab-4d68-87ba-f2ab030011c5
import requests
json_data = requests.get('https://api.rasp.yandex.net/v3.0/search/?apikey=e6bcf177-33ab-4d68-87ba-f2ab030011c5&format=json&from=s9610291&to=s9610287&page=1&date=2025-02-22').json()
print(json_data)

def station_code ():
    '''
    Обское море - 9610291
    Сеятель - 9610470
    Новосибирск-южный - 9610192
    Речной вокзал - 9610287
    Камышенская - 9610219
    '''
    pass
help(station_code)
