import csv
from random import randrange
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
import pandas as pd

for c in range(10):
    cle = rsa.generate_private_key(backend=default_backend(),public_exponent=65537, key_size=512)
    clePublique = cle.public_key().public_bytes(serialization.Encoding.OpenSSH,serialization.PublicFormat.OpenSSH)
    pem = cle.private_bytes(
    format = serialization.PrivateFormat.TraditionalOpenSSL,
    	encoding=serialization.Encoding.PEM,
    	encryption_algorithm = serialization.NoEncryption())
    clePubliqueString = clePublique.decode('utf-8')
    clePriveeString = pem.decode('utf-8')
    with open ("test.csv", "a", encoding = 'utf-8') as file:
        cSV = csv.writer(file)
        cSV.writerow ([clePriveeString,clePubliqueString])
    print(c, "512 RSA clés")
df=pd.read_csv('test.csv')
print ("Doublons : " + str(df.duplicated().sum()))
