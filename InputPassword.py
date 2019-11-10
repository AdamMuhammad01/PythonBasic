'''
contoh program bikin password dengan limit kesalahan
'''
password = '12345'
inputuser = ''
jumlahInput = 1
batasInput = 3
lebih = False

while inputuser != password and not lebih:
    if jumlahInput <= batasInput:
        inputuser = input(f'Input ke-{jumlahInput} ketikan password : ')
        jumlahInput += 1
    else:
        lebih = True
if lebih:
    print("kesempatan anda habis")
else:
    print("password benar")

'''
contoh program bikin password tanpa limit salah
'''
password = '56789'
inputuser1 = ''
while inputuser1 != password:
    inputuser1 = input('Ketikan password : ')
    if inputuser1 != password:
        print('password salah')
    else:
        print('password benar')