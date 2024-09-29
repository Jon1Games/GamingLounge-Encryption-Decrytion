import rsa
import os
import sys
import fnmatch

def open_pub(path):
    with open(path, "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())

def open_priv(path):
    with open(path, "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())
    
def encrypt(file, pub):
    original_text = open(file, "rb").read()
    text = rsa.encrypt(original_text, pub)
    open(file + ".gled", "wb").write(text)
    os.remove(file)

def decrypt(file, priv):
    original_text = open(file, "rb").read()
    text = rsa.decrypt(original_text, priv).decode()
    open(file[:-5], "w").write(text)
    os.remove(file)
    
def isFolder(path):
    if os.path.exists(path):
        if path.endswith("/") or path.endswith("\\"):
            return True
        else:
            return False
        
# Variables
skip = False
mode = 0
filter = ""
keyO = "" 
generateO = ""
encryptO = ""
decryptO = ""

# Checking for help
if sys.argv[1] == "-?" or sys.argv[1] == "--?" or sys.argv[1] == "?" or sys.argv[1] == "help" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
    print("-g <Folder>        | Generate key pair and save as destination")
    print("-e <file/folder>   | Encrypt the file/folder with the public key(The new file name ends with is \".gled\")")
    print("-d <file/folder>   | Decrypt the file/folder with the private key(Only files that end with \".gled\" and matches the filter)")
    print("-f <Pattern>       | Only uses files with spezific pattern, example: \"Test*.txt\"")
    print("-k <key_file>      | Path to key file")

# Collecting arguments
for i in range(1, len(sys.argv)):
    if skip == True:
        skip = False
    elif sys.argv[i] == "-g":
        generateO = sys.argv[i+1]
        skip = True
        mode = 1
    elif sys.argv[i] == "-e":
        encryptO = sys.argv[i+1]
        skip = True
        mode = 2
    elif sys.argv[i] == "-d":
        decryptO = sys.argv[i+1]
        skip = True
        mode = 3
    elif sys.argv[i] == "-f":
        filter = sys.argv[i + 1]
        skip = True
    elif sys.argv[i] == "-k":
        keyO = sys.argv[i + 1]
        skip = True
    elif sys.argv[i] == "-test":
        if fnmatch.fnmatch(sys.argv[i+1], "t*"):
            print("true")
        else:
            print("false")
        skip = True
    else:
        print(sys.argv)

# 
if mode == 1:
    if os.path.exists(generateO):
        if isFolder(generateO):
            name = input("Name: ")
            bit = int(input("Bits: "))
            public, private = rsa.newkeys(bit)
            open(generateO + name + "-private.pem", "wb").write(private.save_pkcs1("PEM"))
            open(generateO + name + "-public.pem", "wb").write(public.save_pkcs1("PEM"))
        else:
            print("This is not an folder.")
    else:
        print("This path does not exists.")

elif mode == 2:
    if os.path.exists(encryptO):
        if os.path.exists(keyO):
            if isFolder(keyO):
                print("A key cannot be a folder!")
            else:
                if isFolder(encryptO):
                    files = os.listdir(encryptO)
                    for f in files:
                        if f.endswith(".gled"):
                            continue
                        elif fnmatch.fnmatch(f, filter):
                            encrypt(encryptO + f, open_pub(keyO))
                else:
                    encrypt(encryptO, open_pub(keyO))
        else:
            print("This path(Key) does not exists!")
    else:
        print("This path(File/s) does not exist!")

elif mode == 3:
    if os.path.exists(decryptO):
        if os.path.exists(keyO):
            if isFolder(keyO):
                print("A key cannot be a folder!")
            else:
                if isFolder(decryptO):
                    files = os.listdir(decryptO)
                    for f in files:
                        if fnmatch.fnmatch(f, filter + ".gled"):
                            decrypt(decryptO + f, open_priv(keyO))
                else:
                    decrypt(decryptO, open_priv(keyO))
        else:
            print("This path(Key) does not exists!")
    else:
        print("This path(File/s) does not exist!")
else:
    print("use -? fpr help")
