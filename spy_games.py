import requests
import time
import json
from pprint import pprint

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
    if 'response' in response.json():
        return response.json()['response']['items']
    else:
        return None


def get_group_by_id(group_id):
    response = requests.get(''.join(('https://api.vk.com/method/groups.getById?group_id=',group_id,'&v=5.52&access_token=', TOKEN)))
    return response.json()['response']


def output(unique_groups):
    ans = []
    for unique_group in unique_groups:
        print('⦁ ⦁ ⦁')
        group = get_group_by_id(str(unique_group))
        
        group_json = {'name':group[0]['name'], 'gid':group[0]['id']}
        ans.append(group_json)
        time.sleep(2)
    ans = json.dumps(ans)
    pprint(ans)


def main():
    user_id = get_id()
    friends = get_friends(user_id)
    user_groups = get_groups(user_id)
    i = 0
    for friend in friends:
        i+= 1
        print('⦁ ⦁ ⦁')
        try:
            for group in get_groups(str(friend)):
                if group in user_groups:
                    user_groups.remove(group)
        except:
            print('Нельзя получить информацию о пользователе {}'.format(friend))
        if i>= 1000:
            break
        time.sleep(1.5)
    output(user_groups)

main()
