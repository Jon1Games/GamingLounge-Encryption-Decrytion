# Gaming Lounge Encrytion Decrytion (GLED)

Both private and public keys are provited for test purpose

## Requirements

- ### Python
- rsa `pip install rsa`<br><br>
or install via rquirements

```
pip install -r requirements.txt
```

## Usage

Command                                         | Usage
----------------------------------------------- | --------------------------------------------
python gled.py -g <destination>               | Generate key pair and save as destination
python gled.py -e <file/folder> <public_key>  | Encrypt the file/folder with the public key
python gled.py -d <file/folder> <private_key> | Decrypt the file/folder with the private key
