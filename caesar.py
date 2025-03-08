# Create a Caesar cipher that encrypts data in a senario where the data would be at a risk of breached
import random
import hashlib
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    encrypted_text = "" 
    for char in text:
        if char.isalpha():
            low_char = char.lower()
            index = letters.index(low_char)
            new_index = (index + shift) % 26
            encrypted_char = letters[new_index]
            if char.isupper():
                encrypted_text += encrypted_char.upper()

            else:
                encrypted_text += encrypted_char
        else:
            encrypted_text += char 
    return encrypted_text        


def decrypt(text, shift):
     decrypted_text = ""
     for char in text:
        if char.isalpha():
            lower_char = char.lower() 
            index = letters.index(lower_char)
            new_index = (index - shift) % 26  
            decrypted_char = letters[new_index]
            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        else:
            decrypted_text += char

     return decrypted_text

def generate_salt(length=16):
    return os.urandom(length).hex()


def generate_hash(text, salt):
    sha256_hash = hashlib.sha256()
    sha256_hash.update((salt+ text).encode('utf-8'))
    return sha256_hash.hexdigest()

def main():
    letter = input("Enter the text for Caesar Cipher: ")
    shift = int(input("Enter the shift value (key): "))
    
    encrypted_text = encrypt(letter, shift)
    print("Encrypted text:", encrypted_text)

    salt = generate_salt()
    encrypted_hash = generate_hash(encrypted_text, salt) 
    print('Salt:', salt)
    print('SHA-256 Hash of the encrypted text', encrypted_hash)                 
  
    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
        main()