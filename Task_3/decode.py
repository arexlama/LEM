import string

alphabet = [x for x in string.ascii_lowercase]
message = 'haqre pbafgehpgvba'

def decode():
    decoded_message = ""
    for i in message:
        if i in alphabet:
            current_letter = alphabet.index(i)
            if current_letter >= 13:
                decoded_message += alphabet[current_letter-13]
            else:
                decoded_message += alphabet[current_letter+13]
        else:
            decoded_message += i
    return decoded_message