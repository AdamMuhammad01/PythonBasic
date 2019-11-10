'''
contoh program mencari isi dictionary
'''
day = {'senin':'monday','selasa':'tuesday','rabu':'wednesday','kamis':'thursday',
'jumat':'friday','sabtu':'saturday','minggu':'sunday'}

hariinput = input('masukan nama hari: ')
print(f'{hariinput.upper()} = {day[hariinput.lower()].upper()}')

'''
contoh program menukar keys & values pada dictionary
'''
days = {'senin':'monday','selasa':'tuesday','rabu':'wednesday','kamis':'thursday',
'jumat':'friday','sabtu':'saturday','minggu':'sunday'}

hari = list(days.keys())
day = list(days.values())
x = input("Ketik nama hari (ENG?IDN) : ")
if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs inggris {x.lower()} adalah {engHari}')
else:
    idDay = hari[day.index(x.lower())]
    print(f'Bhs indonesia {x.lower()} adalah {idDay}')