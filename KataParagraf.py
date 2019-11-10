'''
contoh program menghitung jumlah kata pada paragraf
tanpa menggunakan count
'''
nama = 'Hari ini Hari tidak masuk sekolah karena hari Minggu'
cari = 'i'
x = nama.upper().replace(cari.upper(), '')
jmlCari = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')