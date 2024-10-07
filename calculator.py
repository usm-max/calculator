from addition import add
from  subtraction import sub
from multiplication import mul
from division import div

first = float(input("Enter first number "))
second = float(input("Enter second number "))
print("Enter operator  +  or  /  or  *  or  -   ")
operator = input()

result=0.0
if operator=="+":
    result=add(first,second)
elif operator == "-":
    result=sub(first,second)
elif operator == "*":
    result=mul(first,second)
elif operator == "/":
    result=div(first,second)

print(result)
