
sum1 = 34
def scope():
    # global sum1
    sum1 = 1+1
    # sum1 = sum1 + 32 * 42
    print(sum1)

scope()
print(sum1)