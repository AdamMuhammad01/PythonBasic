'''
if, elif, else
'''
nilai = 55
if nilai > 80:
 print("nilai A")
elif nilai > 60 and nilai < 80:
 print("nilai B")
else :
 print("anda tidak lulus")


'''
contoh soal 
nilai >= 82 : A
nilai 72-81 : B
nilai 62-71 : C
nilai 52-61 : D
nilai <52 : E
'''

nilai = 98
if nilai >= 82:
    print("Nilai Anda A")
elif nilai > 71 and nilai < 82:
    print("Nilai Anda B")
elif nilai > 61 and nilai < 72:
    print("Nilai Anda C")
elif nilai > 51 and nilai < 62:
    print("Nilai Anda D")
else:
    print("Nilai Anda E")