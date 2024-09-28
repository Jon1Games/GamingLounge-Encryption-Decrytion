# Gaming Lounge Encrytion Decrytion (GLED)

## Requirements

- ### Python
- rsa `pip install rsa`<br><br>
  or install via rquirements

```
pip install -r requirements.txt
```

## Usage

| Command                                       | Usage                                        |
| --------------------------------------------- | -------------------------------------------- |
| python gled.py -g <destination>               | Generate key pair and save as destination    |
| python gled.py -e <file/folder> <public_key>  | Encrypt the file/folder with the public key  |
| python gled.py -d <file/folder> <private_key> | Decrypt the file/folder with the private key |

## Cron exmaple

Enxryption every 5 Minutes, then moves the logs into an log archive for better overview and to prevent double encrypting.

```
*/5 * * * * python gled.py -e <logs_folder> <public_key> && mv <logs_folder> <logs_archiv_folder>
```
