# Gaming Lounge Encrytion Decrytion (GLED)

## Requirements

- ### Python
- rsa `pip install rsa`<br><br>
  or install via rquirements

```
pip install -r requirements.txt
```

## Usage

Files that ends with ".gled" cannot be encrypted.<br>
`python gled.py `
| Argument | Usage |
| ---------------- | ------------------------------------------------- |
| -g <destination> | Generate key pair and save as destination |
| -e <file/folder> | Encrypt the file/folder with the public key |
| -d <file/folder> | Decrypt the file/folder with the private key |
| -k <key_file> | Key path |
| -f <filter_end> | use filter, which only apply to the file name end |

## Cron exmaple

Encryption every 5 Minutes, then moves the logs into an log archive for better overview and to prevent double encrypting.

```
*/5 * * * * python gled.py -e <logs_folder> -k <public_key>
```

All files will be encryptet and get the new name: PREVIUS_FILE_NAME.gled
