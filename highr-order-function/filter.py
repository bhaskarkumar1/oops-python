# filter(func,seq)
l = [1, 2, 3, 4, 5]

k = list(filter(lambda x: x % 2 == 0, l))
print(k)
