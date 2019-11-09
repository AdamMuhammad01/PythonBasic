'''
contoh soal balikposisi
'''

x = [1,2,3,4,5]
def balikposisi(mylist):
    hasil = []
    for i in range(len(mylist)):
        hasil.insert(0,mylist[i])
    return hasil

print(balikposisi(x))