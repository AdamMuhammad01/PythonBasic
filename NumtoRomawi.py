'''
contoh class romawi
1 => I
10 => X
3000 => MMM
'''

class romawi:
    def __init__(self,num):
        self.num = num

    def inttoroman(self):
        num_to_roman = [(1000,'M'), (900,'CM'), (500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        res = ''
        for angka, roman in num_to_roman:
            while self.num >= angka:
                res += roman
                self.num -= angka
        return res

roma = romawi(2019)    
print(roma.inttoroman())        
        