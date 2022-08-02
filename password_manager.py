from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  # mode wb-write in Bytes
        key_file.write(key)

    #do not use this function again so the key file remains the same
'''
#write_key()   # call it only once to generate the key.key file


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password: ")
# this master password feature doesnot work
# check it out https://cryptography.io/en/latest/fernet/

key = load_key() + master_pwd.encode()      # encode() turns string into Bytes
fer = Fernet(key)


def view():

    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()            # strips off the line breaker character
            user, passw = data.split("|")   # returns list with 2 elements
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('Password.txt', 'a') as f:    # with automaticly close the file after use,
                                            # do not have manually close the file; a mode append
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Add new password or View existing password (add, view), press q to quit: ")
    mode.lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode! ")
        continue
