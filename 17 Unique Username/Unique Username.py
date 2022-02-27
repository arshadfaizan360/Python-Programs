def generate_username(firstname, lastname):
    username = lastname + firstname[0]

    #check to see if the username already exists
    users_file = open('17 Unique Username\users.txt','r')
    usernames = eval(users_file.read())
    users_file.close()

    for count in range(len(usernames)):
        if usernames[count] == username:
            username = username + '#'
    return username

print(generate_username(input('What is your first name? '),input('What is your last name? ')))