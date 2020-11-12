'''
Caesar Cipher
shifts the letters alphabetically in a given message (input 1) by a number (input 2)
'''
message = input('What is your message? ')
while True:
    shift = input('What number do you want to shift the letters in your message by? ')
    if shift.isdigit():
        break
    else:
        print ('please type a valid integer')
def Cipher(message,shift):
    final_cipher = ''
    for ch in message:
        shift_convert = ord(ch) + int(shift) if ch != ' ' else 32 #to keep spaces
        # Reverts back to A if shifted past Z
        if 90 < shift_convert < 96:
            shift_convert = shift_convert - 26
        # Same thing but for lowercase
        if shift_convert > 122:
            shift_convert = shift_convert - 26
        #converts numbers to characters
        shift_message = chr(shift_convert)
        final_cipher += shift_message

    print('Your new cipher message is: ' + final_cipher)

Cipher(message,shift)
