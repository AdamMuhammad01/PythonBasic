'''
contoh class luas dan keliling persegi
'''

class persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2

persegiA = persegi(4)
persegiB = persegi(8)
persegiC = persegi(10)

print(vars(persegiA)); print(vars(persegiB)); print(vars(persegiC))
