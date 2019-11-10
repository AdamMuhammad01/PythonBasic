'''
program reverse per kata
kalimat = 'Hai aku Tama'
'iaH uka amaT'
'''

kalimat = input('masukan kalimat yg diharapkan : ')
kalimat = kalimat.split()
i = 0
y = []
for i in range(0,len(kalimat)):
    aduh = ''
    aduh = ((kalimat[i]) [::-1])
    y.append(aduh)
    i += 1
y = ' '.join(y)
    
print(y)