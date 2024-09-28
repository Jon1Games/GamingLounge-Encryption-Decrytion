import rsa
import os
import sys
from pathlib import Path

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
    
def isFolder(path):
    if os.path.exists(path):
        if path.endswith("\\"):
            return True
        else:
            return False

goal = sys.argv[1]
if goal == "-?" or goal == "--?" or goal == "?" or goal == "help" or goal == "-help" or goal == "--help":
    print("-g <destination> | Generate key pair and save as destination")
    print("-e <file/folder> <public key> | Encrypt the file/folder with the public key")
    print("-d <file/folder> <private key> | Decrypt the file/folder with the private key")
    isValid = False
elif goal == "-g":
    path = Path(sys.argv[2])
    if os.path.exists(path) and isFolder(path):
        name = input("Name: ")
        bit = int(input("Bits: "))
        public, private = rsa.newkeys(bit)
        open(path + name + "_private.pem", "wb").write(private.save_pkcs1("PEM"))
        open(path + name + "_public.pem", "wb").write(public.save_pkcs1("PEM"))
    else:
        print("This path does not exist or isn´t an folder!")

elif goal == "-e":
    path = Path(sys.argv[2])
    key = Path(sys.argv[3])
    if os.path.exists(path):
        if os.path.exists(key):
            if isFolder(key):
                print("A key cannot be a folder!")
            else:
                if isFolder(path):
                    files = os.listdir(path)
                    for f in files:
                        encrypt(path + f, open_pub(key))
                else:
                    encrypt(path, open_pub(key))
        else:
            print("This path(Key) does not exists!")
    else:
        print("This path(File/s) does not exist!")

elif goal == "-d":
    path = Path(sys.argv[2])
    key = Path(sys.argv[3])
    if os.path.exists(path):
        if os.path.exists(key):
            if isFolder(key):
                print("A key cannot be a folder!")
            else:
                if isFolder(path):
                    files = os.listdir(path)
                    for f in files:
                        decrypt(path + f, open_priv(key))
                else:
                    decrypt(path, open_priv(key))
        else:
            print("This path(Key) does not exists!")
    else:
        print("This path(File/s) does not exist!")

else:
    print("use -? fpr help")
