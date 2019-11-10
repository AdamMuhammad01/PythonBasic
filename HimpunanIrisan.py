'''
contoh program himpunan (antara irisan dan gabungan)
'''
s = set(range(0,12))
a = {2,3,5,7}
b = {5,7,9}

print(a.intersection(b))
print(a.union(b))
print(a.intersection(a.union(b)))
print(b.intersection(a.union(b)))
print(a.union(b).intersection(a.union(b)))
print(a.intersection(b).union(a.union(b)))