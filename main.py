from cryptography.fernet import Fernet
import sys

from rsa import encrypt

def encryptFunc():
    print("ENCRYPTING")
    print("============================================================")
    #open the key file
    with open('filekey.key','rb') as filekey:
        key = filekey.read()
    # using the generated key 
    fernet = Fernet(key)

    # open the file you will encrypt
    with open('textfile.txt','rb') as file:
        original = file.read()
    # encrypt the file  
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and writing the encrypted data
    with open('textfile.txt','wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("FILE ENCRYPTED, CHECK THE FILE")    
    startingFunc()

def decryptFunc():
    print("DECRYPTING")
    print("============================================================")
    # opening the key file 
    with open('filekey.key','rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key) # using the key 
    # open the encrypted file 
    with open('textfile.txt','rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)       #decrypt the file

    # opening the original file and writing the decrypted data 
    with open('textfile.txt','wb') as dec_file:
        dec_file.write(decrypted)
        print("FILE DECRYPTED, CHECK THE FILE")
    
    startingFunc()

def keygenFunc():
    print("KEY GENERATOR")
    key = Fernet.generate_key()     #generate key
    # put the key in a file
    with open('filekey.key','wb') as filekey:
        filekey.write(key)
        print("KEY GENERATED")
    startingFunc()

def startingFunc():
    print("ENCRYPTION AND DECRYPTING")
    print("============================================================")
    print('[1] Generate Key         (note: if there\' already an excisting key for the specific file, using a new key wont decypher your old encrypted txt file)')
    print('[2] Encryption')
    print('[3] Decryption')
    print('[4] Quit')

    while(True):
        choice = int(input("input: "))
        if choice == 0 or choice > 4:
            continue
        elif choice == 1:
            keygenFunc()
            break
        elif choice == 2:
            encryptFunc()
            break
        elif choice == 3:
            decryptFunc()
            break
        elif choice == 4: 
            sys.exit()  
        else:
            continue  

# THE STARTING
startingFunc()     