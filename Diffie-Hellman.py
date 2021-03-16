import pyDH


def dhfunc(otherParty_pubkey):
    key = pyDH.DiffieHellman()
    pubkey = key.gen_public_key()
    sharedkey = key.gen_shared_key(otherParty_pubkey)
    return sharedkey
