#validate username
username = input("pls input your username")
while True:
    if len(username) > 12:
        print("user name not longer 12 digit")
        username = input("pls input your username")
    if username.find(" ") > 0:
        print("user name not longer 12 digit")
        username = input("pls input your username")
    if username.find(".") > 0:
        print("user name not longer 12 digit")
        username = input("pls input your username")
    else:
        print(f"welcome {username}")
        break