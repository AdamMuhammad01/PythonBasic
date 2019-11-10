'''
contoh program menghitung jumlah kalimat pada satu paragraf
tanpa menggunakan count
'''

nama = 'Hari ini Hari tidak masuk sekolah karena hari Minggu'
cari = 'hari'
x = nama.upper().replace(cari.upper(), '')
jmlCari = ((len(nama) - len(x)) / len(cari))
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')