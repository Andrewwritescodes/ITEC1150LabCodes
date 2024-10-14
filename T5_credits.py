def main():
    credits_completed = 15      # Number of credits I will have completed by the end of this semester (not including 20 transferred credits from unrelated major)
    college = 'Minneapolis College'
    report(credits_completed, college)

def report(cr, col):
    print('Your school is', col)
    print(f'You need {60 - cr} credits to graduate')

main()