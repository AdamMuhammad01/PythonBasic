'''
program balik element list
'''

def balikposisi(x):
    y = []
    length = len(x)
    for item in range(length):
        y.append(x[(length-item-1)])
    return y

print(balikposisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikposisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikposisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))