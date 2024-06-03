
letters = 'abcdefghijklmnopsqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    Ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                Ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                Ciphertext += letters[new_index]
    return Ciphertext 

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key 
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index] 
    return plaintext 

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

        for letter in text:
            letter = letter.lower()
            if not letter == ' ':
                index = letters.find(letter)
                if index == -1:
                    result += letter
                else:
                    new_index = index + key
                    if new_index >= num_letters:
                        new_index -= num_letters
                    elif new_index < 0:
                        new_index += num_letters
                    result += letters[new_index]
        return result

    

print()
print('*** CAESAR CIPHER PROGRAM  ***')
print()

print('Choose to encrypt or decrypt')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('YOU HAVE OPTED ENCRYPTION MODE')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the message to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('YOU HAVE OPTED DECRYPTION MODE')
    print()
    key = int(input('Enter the shift key(1 through 26): '))
    text = input ('Enter the message to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')
   