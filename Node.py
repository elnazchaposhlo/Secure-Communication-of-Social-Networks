#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Random import get_random_bytes
from hashlib import sha256

# Here is the Diffie-Hellman computation
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485
g = 2
iv = get_random_bytes(16)
data = b'secure communication for social network'
print(data.hex())

class Node:
    def __init__(self, children=None,parent=None, k):
        if children is None:
            children = []
        else:
            self.children = children
        self.parent = parent
        self.k = k
        self.sessionKeys = []
    x = get_random_bytes(128)
    A = pow(g, x, p)
    def recieveKey(self,key):
        self.sessionKeys.append(key) 
    def sendKey(self,key):
            self.parent.recieveKey(key)
    def populateChildren(self,E):
        children.append(E)
    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children      
# Encrypt the entire data
    def encrypt(self):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(Padding.pad(data, 16))
        print("Ciphertext: {0}\n".format(ciphertext.hex()))

# Decrypt the ciphertext
    def decrypt(self):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext)
        print("Plaintext: {0}".format(Padding.unpad(plaintext, 16)))
    def calculateOwnKey(self):
        pass    
    def calculatekeys(self):
        if len(self.children) == len(self.sessionKeys):
            for index,key in self.sessionKeys:
                result = result ^ key
            result = result ^ self.calculateOwnKey() 
            return result
        else:
            return 0