'''
program sederhana menampilkan bintang2
'''

def star(x):
    star = ''
    for i in range(5):
        star = star + '*'
        print(star)
star(3)

def rstar(x):
    star = ''
    for i in range(x):
        star = '*' * (x-i)
        print(star)
rstar(3)