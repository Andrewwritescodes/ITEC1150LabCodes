# Program to determine if user is eligible to take Apple Mobile programming class
csharp = input('Have you taken C# programming? Type "yes" if so: ')
java = input('Have you taken Java Programming? Type "yes" if so: ')

if csharp == 'yes' + 'Yes' or java == 'yes':
    print('You can take the Apple Mobile Development class.')
else:
    print('Sorry, you need to take either C# or Java before you can take Apple Mobile Development.')