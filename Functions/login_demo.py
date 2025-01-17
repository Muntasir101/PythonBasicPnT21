def login():
    demo_username = "admin"
    demo_password = "123456"

    username = input("Enter your username:")
    password = input("Enter your password:")

    if username==demo_username and password==demo_password:
        print("Login successful")
    else:
        print("Invalid username or password")

login()