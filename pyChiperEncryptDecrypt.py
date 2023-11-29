import json
import base64
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from lzstring import LZString
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
CONS_ID = os.getenv('CONS_ID')

def generate_key(secret_key, cons_id):
    time_stamp = int(time.time())
    return hashlib.sha256(f"{cons_id}{secret_key}{time_stamp}".encode()).digest()

def encrypt(data, secret_key, cons_id):
    key = generate_key(secret_key, cons_id)
    iv = os.urandom(16)
    compressed_data = LZString().compressToEncodedURIComponent(json.dumps(data))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(compressed_data.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode()

def decrypt(encrypted_text, secret_key, cons_id):
    key = generate_key(secret_key, cons_id)
    decoded = base64.b64decode(encrypted_text)
    iv = decoded[:16]
    encrypted_data = decoded[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    decompressed_data = LZString().decompressFromEncodedURIComponent(decrypted.decode())
    return json.loads(decompressed_data)

# Membaca data dari file JSON
with open('sample.json') as json_file:
    data_to_encrypt = json.load(json_file)

# Mengambil data dari string
data_to_encrypt = "Sample Text"

encrypted_text = encrypt(data_to_encrypt, SECRET_KEY, CONS_ID)
print("Encrypt =", encrypted_text, "\n")

decrypted_data = decrypt(encrypted_text, SECRET_KEY, CONS_ID)
print(decrypted_data)
