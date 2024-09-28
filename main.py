import rsa
import os
import sys

def open_pub(path):
    with open(path, "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())

def open_priv(path):
    with open(path, "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())
    
def encrypt(file, pub):
    original_text = open(file, "rb").read()
    text = rsa.encrypt(original_text, pub)
    open(file, "wb").write(text)

def decrypt(file, priv):
    original_text = open(file, "rb").read()
    text = rsa.decrypt(original_text, priv).decode()
    open(file, "w").write(text)

path = sys.argv[1]
if os.path.exists(path):
    if path.endswith("\\"):
        isFolder = True
        folder = path.split("\\")[-2]
    else:
        isFolder = False
        file = path.split("\\")[-1]
    isValid = True
else:
    print("This file/folder does not exist!")
    isValid = False

if isValid == True:
    key = sys.argv[2]
    if os.path.exists(key):
        if key.endswith("\\"):
            print("A key cannot be a folder!")
            isValid = False
        else:
            keyfile = key.split("\\")[-1]
            isValid = True
    else:
        isValid = False
        print("This key file does not exist!")
else:
    pass

if isValid == True:
    if isFolder == True:
        print("1 | Generate Key-pair")
        print("2 | encrypt folder [Public Key]")
        print("3 | decrypt folder [Private Key]")

        mode = input("Enter what you want to do: ")

        if mode == "1":
            name = input("Name: ")
            bit = int(input("Bit-size: "))
            public, private = rsa.newkeys(bit)
            open(path + name + "_private.pem", "wb").write(private.save_pkcs1("PEM"))
            open(path + name + "_public.pem", "wb").write(public.save_pkcs1("PEM"))
        elif mode == "2":
            files = os.listdir(path)
            for f in files:
                encrypt(path + f, open_pub(key))
        elif mode == "3":
            files = os.listdir(path)
            for f in files:
                decrypt(path + f, open_priv(key))
        else:
            print("Your can only enter [1,2,3]")

    elif isFolder == False and isValid == True:
        print("1 | encrypt file [Public Key]")
        print("2 | decrypt file [Private Key]")

        mode = input("Enter what you want to do: ")
        
        if mode == "1":
            encrypt(path, open_pub(key))
        elif mode == "2":
            decrypt(path, open_priv(key))
        else:
            print("You can only enter [1,2]")

    else:
        print("How did you get this error?")
else:
    pass