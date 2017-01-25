from Crypto.PublicKey import RSA
key= RSA.generate(1024)
plik = open('privkey','w')
plik.write(key.exportKey('PEM'))

pubkey = key.publickey()
pub = open('pubkey','w')
pub.write(pubkey.exportKey('PEM'))
