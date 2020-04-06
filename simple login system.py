
def check_if_valid_string(str):
    not_allowed=r" \\"
    if len(str)>36:
        print("password too long")
        return False
    for char in not_allowed:
        if char in str:
            print("invalid character in use")
            return False
    if str =="":
        return False
    return True

def check_if_not_taken(str):
    with open("users.txt") as f:
        content = f.readlines()
        for line in content:
            word = line.split()
            if word[0] == str:
                return False
    return True


f = open("users.txt", "a")
logged_in=False

while logged_in==False:

    a=input("do you have an account? input Y/N\n")

    if a=="N" or a=="n":

        new_mail=input("please input new email no spaces or \ \n")
        if check_if_valid_string(new_mail)==False:
            continue
        if check_if_not_taken(new_mail)==False:
            continue

        new_password=input("please input new password\n")
        if check_if_valid_string(new_password)==False:
            continue

        with open ("users.txt","a") as f:
            f.write(new_mail+" "+new_password+"\n")
        print("now you can login to your account\n")

    elif a=="Y" or a=="y":

        check_mail=input("please input your mail\n")
        check_password = input("please input your password\n")

        with open("users.txt") as f:
            content = f.readlines()
            for line in content:
                word = line.split()
                if word[0] == check_mail:
                    if word[1]==check_password:
                        logged_in = True
                    break

        if logged_in==False:
            print("invalid login credentials")



print("your logged in!")
f.close()

