'''This is ann example key genrator file to generate new RSA keypair using pycrypto
library of python. The key generated using this script will  be saved as mykey.pem
in same directory. 
This example also contains code to read the genarated key and create a object to use it.'''

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
f = open('mykey.pem','wb')
f.write(key.export_key('PEM'))
f.close()

f = open('mykey.pem','r')
key = RSA.import_key(f.read())
print(key)