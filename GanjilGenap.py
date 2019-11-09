'''
contoh program membedakan ganjil / genap
'''
#cara pertama
def ganjilgenap (x):
    if x % 2 == 0:
        print("angka genap")
    else:
        print("angka ganjil")
ganjilgenap(float(input("ketik angka yang diharapkan : ")))

#cara kedua
def ganjilgenap1(angka):
	if angka % 2 == 0:
		return "angka genap"
	else:
		return "angka ganjil"
print(ganjilgenap1(5))

