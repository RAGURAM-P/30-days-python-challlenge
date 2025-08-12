#1.Factorial

def factorial(n):
 if n==0 or n==1:
   return 1
 else:
  return n* factorial(n -1)

num = 5
print("Number:",num)
print("Factorial:",factorial(num))

#2.Prymid pattern Using Nesyted Loop

n =5
for i in range (n+1) :
 for j in range(i):
  print("*",end="")
  print("")
 for i in range (n,0,-1):
  for j in range(i-1):
    print("*",end="")
print("")

#3.Greatest Number

a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
if(a>=b)and(a>=c):
    Largest_Number=a
elif(b>=a)and(b>=c):
    Largest_Number=b
else:
    Largest_Number=c
    print("Largest number is:",Largest_Number)
