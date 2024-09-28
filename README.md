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
python .\main.py .\TestFolder\
```

Encrypt single file

```
python .\main.py .\TestFolder\TestFile .\public
```

Decrypt single file

```
python .\main.py .\TestFolder\TestFile .\private
```

Encrypt all files in an folder

```
python .\main.py .\TestFolder\ .\public
```

Decrypt all files in an folder

```
python .\main.py .\TestFolder\ .\private
```
