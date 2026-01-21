#conditional statements
'''num=10
if num>=1:
    print(num,"+ve")
else:
    print(num,"-ve")
print(type(num))
print(type(num),num)'''

#if number is zero print like "Entered number  is Zero"
'''n=int(input())
if n == 0:
    print("Entered number is Zero")
print("program done")'''

#Check if the number is zero or not
'''num=int(input("enter a number: "))
if num <= 0:
    print("Number is zero")
else:
    print("Number is not zero")'''
    
#even or odd
'''num=int(input("enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")'''

#if elif else
num=int(input("Enter a number: "))
if (num %2 == 0 and num>=0):
    print("positive even")
elif(num %2==0 and num<=0):
    print("Negative even")
elif(num %2 !=0 and  num>=0):
    print("Positive odd")
else:
    print("Negative odd")


 
