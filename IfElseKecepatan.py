'''
contoh program function dengan if else
jika hari ultah maka kecepatan sekarang - 5
'''

def ketangkep(cepet,ultah):
    if ultah:
        kecepatan = cepet - 5
    else:
        kecepatan = cepet

    if kecepatan > 80:
        print('got a big problem')
    elif kecepatan > 60:
        print('dapet himbauan')
    else:
        print('sans aja cuuuy')

ketangkep(84,True)
