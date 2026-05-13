

def max_min(a):
    max_elm = float('-inf')
    min_elm = float('inf')
    for i in range(len(a)):
        if a[i] > max_elm:
            max_elm = a[i]
        
        if a[i] < min_elm:
            min_elm = a[i]
    else:
        print(max_elm, min_elm)



max_min([1,2,6,90,3,5])
