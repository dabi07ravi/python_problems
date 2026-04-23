

a = [
    [1,2],
    [3,4],
    [5,6]
]

b = [[0,0,0],
     [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i] = a[i][j]
else: 
    print(b)

