'''
contoh program menghitung hari
sekarang hari 'rabu', hari apakah 100 hari lagi?
sekarang hari 'rabu', hari apakah 100 hari yang lalu?
'''

hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]
now = "rabu"; brpHari = 100
iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]
print(hariYgDicari)
