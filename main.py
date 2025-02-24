# api key: e6bcf177-33ab-4d68-87ba-f2ab030011c5
import requests
import json
import datetime
dep_input = int(input('Выберите станцию отправления:\n    1) Обское море\n    2) Сеятель\n    3) Новосибирск-южный\n    4) Речной вокзал\n    5) Камышенская\n'))
arr_input = int(input('Выберите станцию прибытия:\n    1) Обское море\n    2)Сеятель\n    3) Новосибирск-южный\n    4) Речной вокзал\n    5) Камышенская\n'))

station_dict = {1:'9610291',
                2:'9610470',
                3:'9610192',
                4:'9610287',
                5:'9610219'}
dep = station_dict.get(dep_input)
arr = station_dict.get(arr_input)

def main():
    if dep == arr:
        return print('Станция прибытия и станция отправления не должны совпадать')

    schedul = requests.get(f'https://api.rasp.yandex.net/v3.0/search/?apikey=e6bcf177-33ab-4d68-87ba-f2ab030011c5&format=json&from=s{dep}&to=s{arr}&page=1&date={datetime.date.today().isoformat()}').json()
    print(schedul)

    dep_time = []
    for i in schedul:
        for train in schedul['segments']:
            dep_time.append(train['departure'][11:16])
            print(train['departure'][11:16], train['duration']/60, train['start_date'])
            if (dep_time[0] == train['departure'][11:16]) and (len(dep_time) > 1): break



def station_code ():
    '''
    Обское море - 9610291
    Сеятель - 9610470
    Новосибирск-южный - 9610192
    Речной вокзал - 9610287
    Камышенская - 9610219
    '''
    pass

if __name__ == '__main__':
    main()
