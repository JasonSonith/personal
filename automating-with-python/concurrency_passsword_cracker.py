import hashlib
import threading
import time
import sys
from pathlib import Path

def create_hash(password):
    hash = hashlib.sha256(password.encode('utf-8'))
    hash = hash.hexdigest()
    return hash

password = "Jasonpw1234"
hash = create_hash(password)

print(f"Password is {password}")
print(f"Hash is {hash}")
