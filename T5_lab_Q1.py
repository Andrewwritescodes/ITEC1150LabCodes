""" Greeting program with capitalized output"""

def greeting(name):
    message = f'Hello {name}!!!!'
    return message.upper()

def main():
    username = 'Andrew'
    hello_message = greeting(username)
    print(hello_message)

main()
