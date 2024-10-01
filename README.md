# Gaming Lounge Encrytion Decrytion (GLED)

## Installation

1. Clone repository
2. Go into the repositorie folder
3. Install python requirements 
```
git clone https://github.com/Jon1Games/GamingLounge-Encryption-Decrytion/
cd GamingLounge-Encryption-Decrytion
pip install -r requirements.txt
```

## Usage

> [!IMPORTANT]
> Files that ends with ".gled" cannot be encrypted.

```
python gled.py [Arguments]
```
| Argument | Usage |
| ---------------- | ------------------------------------------------- |
| -g <destination> | Generate key pair and save as destination |
| -e <file/folder> | Encrypt the file/folder with the public key, ignores ".gled" files |
| -d <file/folder> | Decrypt the file/folder with the private key, generated files end with ".gled" |
| -k <key_file> | Key path |
| -f <filter_end> | Only uses files with spezific pattern, example: \"Test\*.txt\" |
