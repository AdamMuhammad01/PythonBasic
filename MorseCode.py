'''
program input kode morse bolak-balik
'''

morsedict = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'...','i':'..','j':'.---',
'k':'-.-','l':'.-.-','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-',
'v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..', ' ':'/'}

inputuser = input('pesan yg diinginkan: ')
inputuser1 = inputuser.split('#')
duh = ''
if inputuser[0] in morsedict:
    for i in inputuser:
        for a,b in morsedict.items():
            if a == i:
                duh = duh + b
    print(duh)
else:
    for i in inputuser1:
        for a,b in morsedict.items():
            if b == i:
                duh = duh + a
    print(duh)