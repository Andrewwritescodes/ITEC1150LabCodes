def main():

    while user_wants_to_continue('Make squares from words'):
        word = input('Please enter the word to print into a square: ')
        word_square(word)

    print('Thank you for using the square word program!')

def word_square(word):
    for letter in range(len(word)):
        print(word)

def user_wants_to_continue(task):
    response = input(f'Do you want to {task}? Enter "Y" for yes, anything else for no. ')
    if response.upper() == 'Y':
        return True
    return False

main()
