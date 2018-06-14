import requests
import time

APP_ID = 6485129
TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

def get_id():
    id_or_name = input('Введите id или уникальное имя пользователя: ')
    friends=[]
    response = requests.get(''.join(('https://api.vk.com/method/users.get?user_ids=',id_or_name,'&v=5.52&access_token=', TOKEN)))
    user_id = response.json()['response'][0]['id']
    return str(user_id)


def get_friends(user_id):
    response = requests.get(''.join(('https://api.vk.com/method/friends.get?user_id=',user_id,'&v=5.52&access_token=', TOKEN)))
    friends = response.json()['response']['items']
    return friends


def get_groups(user_id):
    response = requests.get(''.join(('https://api.vk.com/method/groups.get?user_id=',user_id,'&v=5.52&access_token=', TOKEN)))
    return response.json()['response']['items']


def main():
    friends = get_friends(get_id())
    for friend in friends:
        print(get_groups(str(friend)))
        time.sleep(int(friend)/100000000)

main()
