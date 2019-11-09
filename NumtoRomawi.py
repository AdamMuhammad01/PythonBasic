'''
contoh program number to romawi
1 => I
10 => X
3000 => MMM
'''

romnum = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,
'V':5,'IV':4,'I':1}
numeral = list(romnum.values())
romawi = list(romnum)
bla = []
def ubah(a):
    while a > 0:
        for i in range (0,len(romnum)):
            if a >= numeral[i]:
                bla.append(romawi[i] * (int(a/numeral[i])))
                a %= numeral[i]
                i += 1
    return ''.join(bla)

print(ubah(2019))