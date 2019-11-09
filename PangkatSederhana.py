'''
program pangkat
'''

def pangkat(num1, num2):
    number = 1  
    for _ in range(num2):   
        number *= num1
    return number

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))