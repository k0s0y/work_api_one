import requests
from datetime import datetime, timedelta
import datetime



def time_calculator(count_of_days_from_today):
    d = datetime.date.today() - timedelta(days=count_of_days_from_today)
    days_from_start = str(datetime.date.today() - d).split(" ")
    date_in_seconds = (int(days_from_start[0]) - 2) * 86400
    return date_in_seconds


if __name__ == '__main__':
    response = requests.get('https://api.stackexchange.com/2.3/questions',
                            params={'site': 'stackoverflow',
                                    'sort': 'votes',
                                    'order': 'desc',
                                    'fromdate': f'{time_calculator(2)}',
                                    'tagged': 'Python'
                                    }
                            )
    for response_ in response.json()['items']:
        print(response_['title'])
