from Crypto.Cipher import AES
# Encryption
def encryptfunc(key,message):
    encryption_suite = AES.new(key, AES.MODE_CBC, 'IV')
    cipher_text = encryption_suite.encrypt(message)
    return cipher_text

# Decryption
def decryptfunc(key,cipher_text):
    decryption_suite = AES.new(key, AES.MODE_CBC, 'IV')
    plain_text = decryption_suite.decrypt(cipher_text)
    return plain_text
