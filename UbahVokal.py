'''
contoh program mengganti huruf vokal dengan 'o'
'''

def ubahvokal(kata):
    output = ''
    for huruf in kata:
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output = output + huruf
    return output
print(ubahvokal('kumaha'))
print(ubahvokal('kambing'))