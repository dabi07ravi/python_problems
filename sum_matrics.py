

a = [[1,2],
     [3,4],
     [5,6]
     ]

b = [[7,8],
     [9,10],
     [11,12]
     ]

c = []

for i in range(len(a)):
    for j in range(len(a[0])):
        sum = a[i][j] + b[i][j]
        c.append(sum)
else:
    print(c)