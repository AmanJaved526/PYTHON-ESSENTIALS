#PRINT PRIME NUMBER IN A GIVEN RANGE
l = int(input("Enter the lower range:"))
u = int(input("Enter the upper range:"))

for num in range(l,u+1):
    if num>1:
        for i in range(2,num):
            if(num%i == 0):
                break
        else:
            print(num, end=" ")

#SUM OF n NUMBERS
n = int(input("Enter the value of n to evaluate the sum:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1

print("Sum:",sum)


# Q3 FACTORIAL OF THE NUMBER
n = int(input("Enter the Number:"))
fact=1
if n<0:
    print("factorial can not be calculated")
else:
    for i in range(1,n+1):
        fact=fact*i

print("Factorial of the number:",fact)

