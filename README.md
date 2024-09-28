# Gaming Lounge Encrytion Decrytion (GLED)

Both private and public keys are provited for test purpose

## Requirements

- ### Python
- rsa `pip install rsa`<br>
  or install via rquirements

```
pip install -r requirements.txt
```

## Usage

Create key pair

```
python .\gled.py .\TestFolder\
```

Encrypt single file

```
python .\gled.py .\TestFolder\TestFile .\public
```

Decrypt single file

```
python .\gled.py .\TestFolder\TestFile .\private
```

Encrypt all files in an folder

```
python .\gled.py .\TestFolder\ .\public
```

Decrypt all files in an folder

```
python .\gled.py .\TestFolder\ .\private
```

|python .\gled.py -g <destination> | Generate key pair and save as destination|
|python .\gled.py -e <file/folder> <public key> | Encrypt the file/folder with the public key|
|python .\gled.py -d <file/folder> <private key> | Decrypt the file/folder with the private key|
