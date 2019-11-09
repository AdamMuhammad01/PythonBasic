'''
contoh program mengganti huruf vokal dengan 'o'
'''
# cara pertama
def ubahvokal(kata):
    output = ''
    for huruf in kata:
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output = output + huruf
    return output
print(ubahvokal('kumaha'))
print(ubahvokal('kambing'))

# cara kedua
def vocal(kalimat):
    kalimat = kalimat.replace('a','o')
    kalimat = kalimat.replace('i','o')
    kalimat = kalimat.replace('u','o')
    kalimat = kalimat.replace('e','o')
    print(kalimat)
vocal("aiueo")
