# encryption and Decryption software

import base64


def encrypt(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if choice in ('e', 'd'):
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")
    
    key = input("Enter the key: ")
    text = input("Enter the text: ")

    if choice == 'e':
        encrypted_text = encrypt(key, text)
        print("Encrypted text:", encrypted_text)
    else:
        decrypted_text = decrypt(key, text)
        print("Decrypted text:", decrypted_text)
        
if __name__ == "__main__":
    main()