master_pwd = input("Enter master password: ")

def add():
    

def view():
    pass

while True:
    mode = input("Would you like to add new password or view existing password? ( add / view ). Enter 'Q' to quit \n").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()

    else:
        print("Enter a valid input.")
    
    break