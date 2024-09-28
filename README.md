# Gaming Lounge Encrytion Decrytion (GLED)

## Requirements

- Python
- rsa `pip install rsa`
  or install via rquirements

```
pip install -r requirements.txt
```

Both private and public keys are provited for test purpose

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
