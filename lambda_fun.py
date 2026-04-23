from functools import reduce

num = int(input('Enter the num: '))


result = list(map(lambda x: x**2, range(1, num+1)))


print("raw_data", result)

filter_data = list(filter(lambda x: x < 40, result))

print("filterr_data", filter_data)


reduce_data = reduce(lambda x, y: x + y, filter_data)


print("reduce_data", reduce_data)



