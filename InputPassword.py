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