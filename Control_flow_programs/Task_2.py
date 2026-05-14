username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Invalid Credentials")
else:
    print("Invalid Credentials")
