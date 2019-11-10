'''
program caesar cipher positif
caesharCipher('Tama',2) => Vcoc
'''

kata = input("masukan kata : ")
jmlpindah = int(input("masukan jumlah huruf yg digeser : "))
alfabet = list('abcdefghijklmnopqrstuvwxyz')
def caesarchipher(x):
    hasil = ''
    for i in kata.lower():
        if i in alfabet:
            step = alfabet.index(i) + jmlpindah
            step = step % len(alfabet)
            hasil += alfabet[(step)]
        else:
            hasil += ' '
    return hasil 
print(caesarchipher(kata))
print(len(alfabet))