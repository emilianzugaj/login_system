import string

letters=string.ascii_letters
numbers=[i for i in range(10)]
special_login_characters="._"
special_password_characters="!@#$%^&*()"
login_characters=letters+str(numbers)+special_login_characters
password_characters=letters+str(numbers)+special_password_characters

password_max_len=16
password_min_len=6
login_max_len=32
login_min_len=3


def check_string_len_in_range(string, max_length=64, min_length=1):
    if len(string) > max_length:
        print("input too long")
        return False
    if len(string) < min_length:
        print("input too short")
        return False
    return True


def check_string_valid_characters(string, valid_characters):
    for char in string:
        if char not in valid_characters:
            print("invalid character in use", '"', char, '"')
            return False
    return True


def check_if_valid_string(string,valid_characters, max_length=16, min_length=6):
    if not check_string_len_in_range(string, max_length, min_length):
        return False
    if not check_string_valid_characters(string, valid_characters):
        return False
    return True


def check_if_not_taken(login, file="users.txt"):
    with open(file) as f:
        content = f.readlines()
        for line in content:
            word = line.split()
            if word[0] == login:
                return False
    return True


def check_if_valid_login_credentials(login, password, file="users.txt"):
    with open(file) as f:
        content = f.readlines()
        for line in content:
            word = line.split()
            if word[0] == login:
                if word[1] == password:
                    return True
                return False


f = open("users.txt", "a")
logged_in = False

while not logged_in:

    a = input("do you have an account? input Y/N\n")

    if a == "N" or a == "n":

        new_login = input("please input new login no spaces or \ \n")
        if not check_if_valid_string(new_login,login_characters,login_max_len,login_min_len):
            continue
        if not check_if_not_taken(new_login):
            continue

        new_password = input("please input new password\n")
        if not check_if_valid_string(new_password,password_characters,password_max_len,password_min_len):
            continue

        with open("users.txt", "a") as f:
            f.write(new_login + " " + new_password + "\n")
        print("now you can login to your account\n")

    elif a == "Y" or a == "y":

        check_login = input("please input your login\n")
        check_password = input("please input your password\n")

        if not check_if_valid_string(check_login,login_characters,login_max_len,login_min_len):
            continue
        if not check_if_valid_string(check_password,password_characters,password_max_len,password_min_len):
            continue

        logged_in = check_if_valid_login_credentials(check_login, check_password)

        if not logged_in:
            print("invalid login credentials")

print("your logged in!")
f.close()
