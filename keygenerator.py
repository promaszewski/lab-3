import rsa
(pubkeya, privkeya) = rsa.newkeys(512, poolsize=2)
print(pubkeya)
print(privkeya)
k=pubkeya.save_pkcs1('PEM')
plik= open('pubkey','w')
plik.write(k)

p=privkeya.save_pkcs1('PEM')
plik= open('privkey','w')
plik.write(p)
