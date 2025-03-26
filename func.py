def func(n):
    if (n%5 == 0):
        return True
    else:
        return False

number = int(input("Enter a number to check if it is divisible by 5: "))
ret_val = func(number)
if ret_val == True:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")