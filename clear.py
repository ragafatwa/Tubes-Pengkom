from os import system, name

def cls():
    # cuman buat bersihkan layar. Aku males nulis ulang2 :v

    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def authenticate_user_input(ans, arr):
    print(ans, arr)