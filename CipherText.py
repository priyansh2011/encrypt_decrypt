# This program illustrates a simple example for encrypting/ decrypting your text

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encrypt(message, key):
    ''' This function lets you to encrypt your message based on a key '''
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            if num>25:
                num=num%25
                num=num-1
            encrypted =encrypted + LETTERS[num]

    return encrypted

def decrypt(message, key):
    ''' This function lets you to decrypt your message based on a key '''
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            if num>25:
                num=num%25
                num=num-1
            num = num -key
            decrypted =decrypted+LETTERS[num]

    return decrypted

def main():
    print("Hello world")

if __name__ == '__main__':
    main()
