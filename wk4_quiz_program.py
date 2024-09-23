# Question 3: While Loops - Quiz Question

print('Quiz program!')

answer = input('What is the capital of Wisconsin? ')  #It's Madison

while answer.upper() != 'MADISON':     # Changing user input to match upper case answer eliminates issue of case sensitivity (MaDiSoN would be correct too)
    print('Sorry, that is not right. Please try again.')    # User answered incorrectly and gets another chance
    answer = input('What is the capital of Wisconsin? ')    # User answered correctly and prompts the "correct" statement to run

print('That is correct!')   # This is the "correct" statement