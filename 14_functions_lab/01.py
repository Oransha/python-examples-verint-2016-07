def my_sum(*numbers):
    sum_num = 0
    for n in numbers:
        if type(n) is int:
            sum_num += n
    return sum_num

print my_sum(1,2,3, "bob")

def my_multi(*numbers):
    multi_num = 1
    for n in numbers:
        if type(n) is int:
            multi_num *= n
    return multi_num

print my_multi(1,2,3,4, "bob")        