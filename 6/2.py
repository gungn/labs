result = 4 ** 2020 + 2 ** 2017 - 15

binar = bin(result)[2:]

count_ones = binar.count('1')

print(count_ones)
