import requests


def how_smart_hero(heroes):
    hero_intelligence = {}
    for hero in heroes:
        url = f'https://superheroapi.com/api/{TOKEN}/search/{hero}'
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Запрос не успешен {response.status_code}')
            return
        else:
            name = response.json()['results'][0]['name']
            intelligence = response.json()['results'][0]['powerstats']['intelligence']
            hero_intelligence[name] = intelligence
    smart_hero = max(hero_intelligence)
    print(f'Самый умный супергерой "{smart_hero}" уровень его разума равен {hero_intelligence[smart_hero]}')


if __name__ == '__main__':
    TOKEN = 2619421814940190
    list_of_heroes = ['Hulk', 'Captain America', 'Thanos']
    how_smart_hero(list_of_heroes)
