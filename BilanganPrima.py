'''
bilangan prima dari 1 - 100
2,3,5,7,11,...
'''
def prima(x):
    if x > 1:
        if x == 2:
            a= True
        else:
            for i in range(2,x):
                if x % i == 0:
                    a= False
                    break
                else:
                    a= True
    else:
        a= False
    return a

print(prima(97))
