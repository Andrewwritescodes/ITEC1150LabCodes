def is_password_long_enough(password):
    if len(password) >= 8:
        return True
    else:
        return False

def main():
    password = 'Dragonforce'
    password_long_enough = is_password_long_enough(password)
    if password_long_enough == True:
        print(f' The password "{password}" is long enough')
    else:
        print(f' The password "{password}" is NOT long enough')

main()