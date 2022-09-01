from twofish import Twofish

def tfencrypt(infile, outfile, password):

    bs = 16 #block size 16 bytes or 128 bits 
    plaintext=infile.read()

    if len(plaintext)%bs: #add padding 
        padded_plaintext=str(plaintext+'%'*(bs-len(plaintext)%bs)).encode('utf-8')
    else:
	    padded_plaintext=plaintext.encode('utf-8')
        
    T = Twofish(str.encode(password))
    ciphertext=b''

    for x in range(int(len(padded_plaintext)/bs)):
	    ciphertext += T.encrypt(padded_plaintext[x*bs:(x+1)*bs])
        
    outfile.write(ciphertext)


password = '12345'

with open('infile.txt', 'r') as infile, open('outfile.txt', 'wb') as outfile:
    tfencrypt(infile, outfile, password)
