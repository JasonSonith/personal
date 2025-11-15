import hashlib
from os import path
import threading
import time
import sys
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--wordlist", type=str,required=True)
parser.add_argument("--hash", type=str, required=True)

args = parser.parse_args()
wordlist_path = Path(args.wordlist)
obtained_hash = (args.hash)

if not wordlist_path.exists():
    print(f"Error: Wordlist '{args.wordlist}' not found!")
    print(f"Please check the path and try again.")
    sys.exit(1)

def create_hash(password):
    hash = hashlib.sha256(password.encode('utf-8'))
    hash = hash.hexdigest()

def check_hash(chunk,obtained_hash):
    for i in chunk:
        hash = create_hash(i)
        if obtained_hash == hash:
            return hash
    return None

def process_chunks(chunks):
    pass
