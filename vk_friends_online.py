import vk
from getpass import getpass

APP_ID = 6307155


def get_user_login():
    login = input('Please enter your login: ')
    return login


def get_user_password():
    password = getpass('Please enter your password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_ids = api.friends.getOnline()
    friends_online_list = api.getProfiles(user_ids=friends_ids)
    return friends_online_list


def output_friends_to_console(friends_online_list):
    print('Friends currently online:')
    if friends_online_list:
        for friend in friends_online_list:
            print(friend['first_name'], friend['last_name'])
    else:
        print('There are no friends online')


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
