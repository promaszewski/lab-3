#!/usr/bin/env python
import hashlib
import ssdeep
plik= open('rsaprogram.zip','rb')
try:
    aplik1= plik.read();
finally:
    plik.close()
m=hashlib.sha256(aplik1).hexdigest()
print("SHA 256")
print(m)
s=hashlib.md5(aplik1).hexdigest()
print("MD 5")
print(s)
ssdp= ssdeep.hash(aplik1)
print("ssdeep")
print(ssdp)
blocksize=65535
o=" "
with open('rsaprogram.zip',"rb") as f: 
	for b in iter(lambda: f.read(1025),""): 
		md5dp=hashlib.md5(b)
		o=o+md5dp.hexdigest()
print("md5deep")
print(o)
