'''
program buat kode morse
'''
morsedict = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'...','i':'..','j':'.---',
'k':'-.-','l':'.-.-','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-',
'v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..', ' ':'/'}

duh = input('masukan kalimat : ')
def morse(x):
    y=''
    for i in x.lower():
        y = y + ' ' + (morsedict.get(i))
    return y
print(morse(duh)) 