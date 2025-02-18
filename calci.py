#done
num1= input('enter first number:' )
num2= input('enter second number:' )
sum = float(num1) + float(num2)
print('the sum of {0} and {1} is {2}'.format(num1,num2,sum))


num1=input("enter the first number ")
num2=input("enter the first number ")
num3=input("enter the first number ")

# def max_num(num1, num2, num3):
if num1 >=num2  and num1 >=num3:
        print(f"first number {num1} is largest")
        # return num1
elif num2 >=num1 and num2 >=num3:
        print(f"second number {num2} is largest")
        # return num2
else:
        print(f"third number {num3} is largest")

# print(max_num)
