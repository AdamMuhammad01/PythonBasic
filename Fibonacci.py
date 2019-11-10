'''
buatlah deret fibonacci sederhana
'''

def fibonacci(x):
    listdata = [1,1]
    for i in range(2,x):
        listdata.append(listdata[i-2] + listdata[i-1])
    return listdata[x-1]

print(fibonacci(8))