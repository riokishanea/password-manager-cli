import cryptocode
import os
#test
master_pwd = input("Enter master password to enter the vault: ")

def add():
    user_name = input("Username: ")
    user_pwd = input("Password: ")

    encrypted_pwd = cryptocode.encrypt(user_pwd, master_pwd)

    with open('password.txt', 'a') as f:
        f.write(user_name + "|" + encrypted_pwd + "\n")

    print(f"Success! Saved password for {user_name}")

def view():

    if not os.path.exists('password.txt'):
        print("Vault is empty, No passwords saved yet.")
        return
    
    try:
        with open('password.txt','r') as f:

            lines = f.readlines()

            if len(lines) == 0:
                print("Vault is empty, Add a password first!")
                return

            for line in lines:
                data = line.strip()
                u_name, u_enc_pwd = data.split("|")

                decoded_pwd = cryptocode.decrypt(u_enc_pwd, master_pwd)

                if decoded_pwd:
                    print("Username:",u_name + "\n" + "Password:", decoded_pwd )
                    print()
                else:
                    print("Username:",u_name + "\n" + "Password: [LOCKED - Wrong key]",)

    except FileNotFoundError:
        print("No passwords saved yet!")


while True:
    mode = input("---- Vault Menu ---- \n\nAdd / View / Quit (Q) \n\nEnter a option to continue : ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Enter a valid input.")