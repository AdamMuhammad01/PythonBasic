'''
palindrome
katak = katak    True
malam = malam    True
bantal = latnab  False
'''

x = 'katak'

def palindrome(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False
print(palindrome(x))