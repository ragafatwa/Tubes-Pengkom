import hashlib

data = {
    'user': '97ef4217cec896792c0c518addd05cd2',
    'admin': '537e50a52d92c948966a42563a3f95ab',
    '1234':'505942616eb7f21f0155e7facab17d35'
}

def check_credential(user, password):
    if user in data:
        salt = '5gz'
        password = password + salt
        hashed = hashlib.md5(password.encode())
        hashed = hashed.hexdigest()

        if hashed == data[user]:
            return [True, user]
    return [False, 1]