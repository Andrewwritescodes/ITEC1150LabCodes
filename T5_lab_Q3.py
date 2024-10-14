""" Program to determine if user can upgrade to Windows 11"""

def windows_11_compatible(memory, storage_space, current_os):    # Function to define requirements for upgrade to Windows 11
    if memory >= 8 and storage_space >= 64 and current_os.lower() == 'windows 10':  # The minimum requirements for upgrade
        return True
    else:
        return False


def main():
    memory = int(input('Enter your current memory in GB: '))
    storage_space = int(input('Enter your current amount of free storage space in GB: '))
    current_os = input('Enter your current operating system: ')

    can_upgrade = windows_11_compatible(memory, storage_space, current_os)  # Checks that user's conditions meet the minimum upgrade requirements

    if can_upgrade:
        print('You are eligible for an upgrade to Windows 11')
    else:
        print('You are not eligible for an upgrade')


main()