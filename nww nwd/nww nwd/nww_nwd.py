def nwd(num1, num2):
    while num1 != num2:
        if(num1 > num2):
            num1 -= num2
        else:
            num2 -= num1
    return num1

def nww(num1, num2):
    return num1 * num2 / nwd(num1, num2)

print(nwd(12, 16))
print(nww(12, 16))