""" 
	URI Online Judge 
	Problema 1253 - Cifra de César
    https://www.urionlinejudge.com.br/repository/UOJ_1253.html
 """

def decodeText(text, offset): 
    decode = ""
    for letter in text:
        value = ord(letter) - int(offset)
        if value < 65:
            value += 26
        decode += chr(value)
    return decode

num = input()

for i in range(0, int(num)):
    text = input()
    offset = input()
    decode = decodeText(text, offset)
    print(decode)
