'''
program faktorial
'''
def faktorial(x):
    if x == 0:
        return 1
    else:
        return x*faktorial(x-1)
print(faktorial(4))

def faktorial2(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    return angka
print(faktorial2(3))


def faktorial3(x):
    if x <= 2:
        return x
    else:
        return x * faktorial3(x-1)
print(faktorial3(3))