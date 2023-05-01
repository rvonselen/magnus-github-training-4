def fibonacci(n):
    i = 0
    i1 = 0
    i2 = 1
    string = '0 '
    while i < n:
        string = string + str(i2) + ' '
        i_store = i2
        i2 = i1 + i2
        i1 = i_store
        i += 1
    return string
print(fibonacci(15))