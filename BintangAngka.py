'''
1               1               5
1 2             2 2             5 4
1 2 3           3 3 3           5 4 3
1 2 3 4         4 4 4 4         5 4 3 2
1 2 3 4 5       5 5 5 5 5       5 4 3 2 1

1 2 3 4 5       1 1 1 1 1       5 4 3 2 1
1 2 3 4         2 2 2 2         5 4 3 2
1 2 3           3 3 3           5 4 3
1 2             4 4             5 4
1               5               5
'''


############### tengah ######################

for column in range(1,6):
    for rows in range(column):
        print(column, end=' ')
    print('')

for column in range(1,6):
    for rows in range(6-column):
        print(column, end=' ')
    print('')

############## kiri #############################
for column in range(1,6):
    for rows in range(column):
        print(rows+1, end= ' ')
    print('')

for column in range(5):
    for rows in range(5-column):
        print(rows+1, end= ' ')
    print('')

############### kanan ############################
for column in range(5,0,-1):
    # print("ini",column)
    for rows in range(5, column-1,-1):
        print(rows, end= ' ')
    print('')

for column in range(1,6,1):
    # print("ini",column)
    for rows in range(5, column-1,-1):
        print(rows, end= ' ')
    print('')