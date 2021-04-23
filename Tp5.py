def defahacel():
    farenheit = []
    celsius = []
    i = 0
    while i <= 120:
        farenheit.append(i)
        i = i + 10
    i = 0
    while i <= 12:
        numcelsius = (farenheit[i] - 32) / (9 / 5)
        celsius.append(numcelsius)
        i = i + 1
    return farenheit, celsius
print (defahacel())