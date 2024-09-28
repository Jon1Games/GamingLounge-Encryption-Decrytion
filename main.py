import rsa

def open_pub():
    with open(input("Enter public key: "), "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())

def open_priv():
    with open(input("Enter private key: "), "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())

print("1 | decrypt file")
print("2 | encrypt file")
mode = input("Enter what you want to do: ")
if mode == "1":
    priv = open_priv()
    file = input("file: ")
    original_text = open(file, "rb").read()
    text = rsa.decrypt(original_text, priv).decode()
    open(file, "w").write(text)
elif mode == "2":
    pub = open_pub()
    file = input("file: ")
    original_text = open(file, "rb").read()
    text = rsa.encrypt(original_text, pub)
    open(file, "wb").write(text)
else:
    print("You can only enter [1,2]")
