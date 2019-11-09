'''
bikin function fizzBuzz dgn 1 parameter
tampilkan angka 1 - 15
bilangan kelipatan 3 = fizz
bilangan kelipatan 5 = buzz
bilangan kelipatan 3 & 5 = fizzbuzz
'''

def fizzbuzz(x):
    for i in range(1,x+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz(15)