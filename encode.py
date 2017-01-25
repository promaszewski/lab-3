import rsa
key=open('pubkey','r')
klucz=key.read()
pub =  rsa.PublicKey.load_pkcs1_openssl_pem(klucz)
from rsa.bigfile import *
with open('rsaprogram.zip', 'rb') as infile, open('encode.txt', 'wb') as outfile:
	encrypt_bigfile(infile, outfile, pub)
plik= open("encode.txt","r")

plik1= plik.read()
plik.close()
from binascii import unhexlify
aplik= open("encode.txt","w")
aplik.write(plik1.encode("hex"))
aplik.close()
