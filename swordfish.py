while True:
    print('Who are you')
    name = input()
    if name != 'Nik':
        continue
        print('Hello Nik, what is the password (it is a fish)')
        password = input()
        if password == 'swordfish':
            break
            print('Access granted')


