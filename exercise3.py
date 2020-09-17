a = [5, 6, 2, 646, 567, 223, 90]

i = 0
sum = 0

def sum_1(array):
    i = 0
    sum = 0

    while i < len(a):
        sum +=a[i]
        i += 1

    print(sum)

def sum_2(array):
    sum = 0

    for j in a:
        sum += j
    print(sum)

def sum_3(array):

    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_3(array[1:])

sum_1(a)
sum_2(a)
print(sum_3(a))