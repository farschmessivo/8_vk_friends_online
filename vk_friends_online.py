import vk
from getpass import getpass

APP_ID = 6307155


def get_user_login():
    print('Please enter your login: ')
    login = input()
    return login


def get_user_password():
    print('Please enter your password: ')
    password = getpass()
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',   # <===== I don't get it
    )
    api = vk.API(session)
    friends_ids = api.friends.getOnline()
    friends_online_list = api.getProfiles(user_ids=friends_ids)
    return friends_online_list


def output_friends_to_console(friends_online_list):
    for friend in friends_online_list:
        friend_first_name = friend.get('first_name')
        friend_last_name = friend.get('last_name')
        print(friend_first_name, friend_last_name)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
