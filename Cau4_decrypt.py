import base64
from Crypto.Cipher import AES
key = b'This is the super secret key 123'

encrypted_text = 'v/sJpihDCo2ckDmLW5Uwiw==&#10'
cipher = AES.new(key, AES.MODE_CBC, b'\x00'*16)

decoded = base64.b64decode(encrypted_text)
decrypted = cipher.decrypt(decoded)

print(decrypted)