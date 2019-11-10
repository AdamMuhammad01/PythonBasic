'''
membuat class untuk mean, median dan modus secara manual
'''
class statistika:
    def mean(self,x):
        y = sum(x) / len(x)
        return y
    def median(self,x):
        x.sort()
        if len(x) % 2 == 0:
            y = (((x[(len(x))/2]) + (x[(((len(x))/2))-1]))/2)
        else:
            y = (x[((len(x))/2)])
        return y
    def modus(self,x):
        default = 0
        angka = 0
        for y in x:
            if x.count(y) > default:
                default = x.count(y)
                angka = y
        return angka
duh = statistika()
print(duh.median([10,3,2,8,5,4,6,8,7,9]))