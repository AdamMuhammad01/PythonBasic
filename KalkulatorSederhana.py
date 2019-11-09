'''
contoh program membuat kalkulator
'''

def calc():
    x = float(input("masukan angka pertama : "))
    op = input("masukan operator yang digunakan : (+-*/) ")
    y = float(input("masukan angka kedua : "))
    if op == '+':
        print(x+y)
    elif op == '-':
        print(x-y)
    elif op == '*':
        print(x*y)
    elif op == '/':
        print(x/y)
    else:
        print("Maaf operator tidak dikenali")
calc()