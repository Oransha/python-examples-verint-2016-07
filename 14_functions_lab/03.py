def tens(*numbers):
    sum = 0
    for n in numbers:
        sum += ((n%100)/10)
    return sum

print tens(1120, 120,240)

