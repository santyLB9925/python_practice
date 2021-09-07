def multiple(num):
    if(num % 4 == 0):
        return print("Also ",num ,"is multiple of 4")
    else:
        return print(num," it is not multiple of 4")
def divisor(num,check):
    if num % check == 0:
        print(num, "divides evenly by", check)
    else:
        print(num, "does not divide evenly by", check)

num = int(input("Enter a number: "))
check = int(input("Give me a number to divide by: "))
if(num % 2 == 0):
    print("Even number")
    multiple(num)
    divisor(num,check)
else:
    print("Odd number")
    multiple(num)
    divisor(num,check)

