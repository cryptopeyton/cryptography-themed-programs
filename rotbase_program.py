#  Peyton Thomas
#  ROT13 and B64 encoding program

import base64

#  Dictionary to look up index of alphabets
dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
         'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
         'Z': 26}
dict2 = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
         13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
         25: 'Y', 26: 'Z'}


#  Rot13 encrypt function block
#  according to shift provided
def encrypt(message, shift):
    cipher = ''
    for letter in message:
        #  checking for space
        if letter != ' ':
            #  looks up the dictionary index and adds shift to index
            num = (dict1[letter] + int(shift)) % 26
            #  looks up the second dictionary for the shifted alphabet and adds them
            cipher += dict2[num]
        else:
            #  adds space
            cipher += ' '

    return cipher


#  Function to decrypt the string
#  according to the shift provided
def decrypt(message, shift):
    decipher = ''
    for letter in message:
        #  checks for space
        if letter != ' ':
            #  looks up the dictionary and subtracts the shift to the index
            num = (dict1[letter] - int(shift) + 26) % 26
            # looks up 2nd dictionary and subtracts the shift to the index
            decipher += dict2[num]
        else:
            #  adds space
            decipher += ' '

    return decipher


#  Base64 encrypt function block with rot13 parameter
def encode_base64_text(normal_rot13_text):
    encoded_normal_text = normal_rot13_text.encode('ascii')  # encodes it in ascii?
    encoded_text = base64.b64encode(encoded_normal_text)  # encode var that stored string in b64
    encoded_text_message = encoded_text.decode('ascii')
    return encoded_text_message


#  Base64 decode function block
def decode_base64_text():
    decoded_text_input = input("Please enter the encoded text: ")
    decoded_text_ascii = decoded_text_input.encode('ascii')
    decode_text = base64.b64decode(decoded_text_ascii)
    decoded_ascii_text = decode_text.decode('ascii')
    print(decoded_ascii_text)
    return decoded_ascii_text


#  for def main(), do the rot13 sequence first, then put the var of the rot13 into the base64 sequence, you main have to
#  include parameters for the base64 code to do, so that instead of the input you put a variable for the sequence. 
#  or go b64 first followed by the rot13 and adding the b64 text into the
#  rot13 function, or we could just make it one big joint, idk.

def main():
    # use upper() to convert char
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1, 2): "))
    # first choice for encrypting a plaintext message
    if choice == 1:
        nonrot13_message = str(input("Please input the message here: "))
        first_shift = int(input("Please enter the shift number here, ex: 13: "))
        first_result = encrypt(nonrot13_message.upper(), first_shift)
        rotbase_text = encode_base64_text(first_result)
        print(rotbase_text)
    # second choice for decoding text
    elif choice == 2:
        decode_base64_text()
        rot13_message = str(input("Please enter previous encrypted message here: "))
        shift_number = int(input("Please enter the shift number here, ex: 13: "))
        decoded_rot13_text = decrypt(rot13_message.upper(), shift_number)
        print(decoded_rot13_text)


if __name__ == "__main__":
    main()
