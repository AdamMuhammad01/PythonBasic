'''
nomor = 1-100
=> angka genap(filter)
[2,4,6,8,...]
=> setiap angka genap x2 (map)
[4,8,12,...]
=> setiap angka hasilnya dijumlahkan satu sama lain(reduce)
4+8+12+...
'''

angka = range(1,102)
from functools import reduce
z = reduce(lambda num,num1: num+num1,map(lambda num:num*2,filter(lambda num: num%2==0,angka)))
print(z)