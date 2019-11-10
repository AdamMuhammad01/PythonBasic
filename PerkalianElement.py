'''
contoh program mengalikan element list
'''
# cara pertama
ancyur = [1,2,3,4,5]
print(list(map(lambda num: num*2,ancyur)))

# cara kedua
x = [1,2,3,4,5,6,7,8,9,10]
y = []
index = 0
while index < len(x):
    y.append(x[index] ** 2)
    index += 1
print(y)