'''
program pangkat
'''

def pangkat(num1,num2):
    number = 1
    for _ in range(num2):
        number *= num1
    return number
print(pangkat(2,3))

def pangkat1(x,y):
    if y ==0:
        return 1
    else:
        return x*pangkat(x,y-1)
        
print(pangkat1(0,3))