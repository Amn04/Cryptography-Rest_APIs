from twofish import Twofish

def tfdecrypt(infile, outfile, password):

    bs = 16 #block size 16 bytes or 128 bits
    ciphertext = infile.read()
    T = Twofish(str.encode(password))
    plaintext=b''

    for x in range(int(len(ciphertext)/bs)):
        plaintext += T.decrypt(ciphertext[x*bs:(x+1)*bs])

    outfile.write(str.encode(plaintext.decode('utf-8').strip('%'))) #remove padding

password = '12345'


with open('outfile.txt', 'rb') as infile, open('outfile_decrypted.txt', 'wb') as outfile:
    tfdecrypt(infile, outfile, password)