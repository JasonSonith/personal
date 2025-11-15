import hashlib
import threading
import time
import sys
from pathlib import Path

def create_hash(password):
    hash = hashlib.sha256(password.encode('utf-8'))
    hash = hash.hexdigest()

def process_chunks(chunks):
    pass
