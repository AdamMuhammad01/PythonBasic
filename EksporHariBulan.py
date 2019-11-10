'''
buat file py => class/object
kemudian tampil di file y.py
waktu.hari = 
waktu.tanggal = 
waktu.bulan =
waktu.tahun = 
waktu.jam = 
waktu.menit = 
waktu.detik =
'''

import datetime as dt
x = dt.datetime.now()
listHari = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu',
'Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'}
listBulan = {'January':'Januari','February':'Februari','March':'Maret',
'April':'April','May':'Mei','Juny':'Juni','July':'Juli','August':'Agustus',
'September':'September','October':'Oktober','November':'Nopember','December':'Desember'}
class sekarang:
    def __init__(self):
        self.tanggal = x.strftime('%d')
        self.tahun = x.strftime('%Y')
        self.jam = x.strftime('%H')
        self.menit = x.strftime('%M')
        self.detik = x.strftime('%S')
        self.hari = listHari[x.strftime('%A')]
        self.bulan = x.strftime('%m')
        self.namabulan = listBulan[x.strftime('%B')]
nama = 'andi'
waktu = sekarang()