from math import floor


def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values

def inverter(array):
    new_array = []
    for i in range(len(array)):
        new_array.append(array[len(array) - (i+1) ])
    return new_array


repeticoes = int(input())
for i in range(repeticoes):
    text = input()
    textToAscii = to_ascii(text)



    for i in range(len(textToAscii)):
        if(textToAscii[i] >= 65 and textToAscii[i] <= 90) or (textToAscii[i] >= 97 and textToAscii[i] <= 122):
            textToAscii[i] = textToAscii[i] + 3



    textToAscii_invert = inverter(textToAscii)



    metade = floor(len(textToAscii_invert)/2)



    for i in range (metade , len(textToAscii_invert)):
        textToAscii_invert[i] = textToAscii_invert[i] -1

    textToAscii_invert_to_string = []
    for i in range(len(textToAscii_invert)):
        textToAscii_invert_to_string.append(chr(textToAscii_invert[i]))


    crypted = ''.join(textToAscii_invert_to_string)

    print (crypted)
