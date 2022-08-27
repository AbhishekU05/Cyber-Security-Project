# Dictionary of all the usernames and passwords
uid = {
    'abhishek': '1234',
    'taran': 'abcde',
    'sachin': 'password',
    'nitin': 'nitin',
    'puneet': 'abc@123',
    'tushar': 'hello123',
    'Dictionary_values': '97621!'
}
l = len(uid)  # length of dictionary

user = input("Enter username:\n")  # variable for storing username
password = input("Enter password:\n")  # variable for storing password

# nested if construct to check the entered username and password
if user in uid:
    if password == uid[user]:
        print("\n\nWelcome ", user, "\n")
        print("\t\t\tGOOGLE\n")
        print("Search:_\n\n")
    else:
        print("Invalid username or password")
    if user == 'Dictionary_values' and password == uid[user]:
        print("Username   Passwords")
        for i in uid:
            print(i, ':', uid[i])
else:
    print("Invalid username or password")
