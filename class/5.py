
user1 = {
    'status': 'active',
    'name' : 'FIO'
}

user2 = {
    'status': 'offline',
}

def wrapper(func):

    def a(user):
        if user['status'] == 'offline':
            print("User not authorized")
        else:
            func(user)
    
    return a

import datetime


def log(func):

    def a(*args, **kwargs):
        print(f'Function was called at {datetime.datetime.now()}')
        func(*args, **kwargs)

    return a


# @log
# @wrapper
def hello(user):
    print('Hello, ',user['name'])

hello = wrapper(hello)
hello = log(hello)

hello(user1)
hello(user2)