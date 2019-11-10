'''
import statistics
x = [1,3,9,2,6,4,7,8,5,5]

print(statistics.mean(x))
print(statistics.median(x))
print(statistics.mode(x))

buat program diatas tanpa import statistic
'''

from functools import reduce
class statistik:
    def rataRata(self,x):
        total = reduce(lambda a,b:a+b,x)
        return total/len(x)
    def nilaiTengah(self,x):
        x.sort()
        if len(x) % 2 != 0:
            iTengah = [int(len(x)/2)]
        else:
            iTengah = [int(len(x)/2)-1, int(len(x)/2)]
        aTengah = list(map(lambda a:x[a], iTengah))
        total = reduce(lambda x,y:x+y, aTengah)
        return total/len(aTengah)
    def modus(self,x):
        hitung = list(map(lambda a: x.count(a),x))
        iMax = hitung.index(max(hitung))
        return x[iMax]
        
stat = statistik()
print(stat.modus([10,3,3,8,5,4,6,8,7,9]))