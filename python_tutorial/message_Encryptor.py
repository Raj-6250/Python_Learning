# message encryptor and decryptor

import random
import string

char = " " + string.punctuation + string.digits +  string.ascii_letters
new_char = list(char) # it typecast character into list
key =new_char.copy()  # it create a copy of original
random.shuffle(key)   # it shuffle the list of key

print(f"char : {new_char}")
print(f"key  : {key}")

#Encrypt
plain_text = input("Enter message to encrypt : ")
cipher_text = ""

for letters in plain_text :
    index = new_char.index(letters)
    cipher_text = cipher_text + key[index]

print(f"Original message  : {plain_text}")
print(f"Encrypted message : {cipher_text}")


#Decrypt
cipher_text = input("Enter message to decrypt : ")
plain_text = ""

for letters in cipher_text :
    index = key.index(letters)
    plain_text = plain_text + new_char[index]

print(f"Encrypted message : {cipher_text}")
print(f"Original message  : {plain_text}")

