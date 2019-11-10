'''
contoh program sistem persamaan linear dua variabel
#jmlhewan = 13
#jmlkaki = 32
#kakiayam = 2
#kakikambing = 4
'''

#cara 1 dengan input angka manual
jmlhewan = input('masukan total hewan? : ')
jmlkaki = input('masukan total kaki hewan? : ')
kakiA = input('masukan jumlah kaki hewan A? :')
kakiB = input('masukan jumlah kaki hewan B? :')
ayam = (int(jmlkaki) - (int(kakiB) *int(jmlhewan))) / int(int(kakiA) - int(kakiB))
kambing = (int(jmlkaki) - (int(kakiA) *int(jmlhewan))) / int(int(kakiB) - int(kakiA))
print(f'jumlah hewan A = {ayam}, jumlah hewan B = {kambing}')

#cara kedua dengan input angka yg sudah ditentukan
jmlhewan = 13; jmlkaki = 32; kakiA = 2; kakiK = 4
A = (jmlkaki - (kakiK *jmlhewan)) / (kakiA - kakiK)
K = (jmlkaki - (kakiA *jmlhewan)) / (kakiK - kakiA)
print(f'Jumlah ayam = {A}')
print(f'Jumlah kambing = {K}')