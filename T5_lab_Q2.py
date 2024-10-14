""" Quiz program where main function calls quiz function twice"""

def quiz(question, correct_answer): # quiz function with 2 parameters for question and correct answer
    print(question)
    user_answer = input('Answer: ')

    if user_answer.upper() == correct_answer.upper():   # Correcting for case sensitivity in user_answer input
        print('That is correct!')
    else:
        print('Sorry that is incorrect')        # This will print if user_answer != correct_answer

def main(): # Main function will call quiz function twice
    quiz('Is Pluto a planet?', 'NO')    # Pluto is a dwarf planet
    quiz('What is the name for a group of owls?', 'PARLIAMENT')

main()