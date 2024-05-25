'''my_file = open("gee.txt","w")
my_file.write("python is the best for dsa")
my_file.close()

# lets read the content in python?

 
my_file = open("gee.txt","r")
print(my_file.read()) '''

# write a program to take number from users and  add those number?

"""x = int(input("enter the value A:"))
print(x)

y = int(input("enter the value B:"))
print(y)

sum = x+y
print (sum)"""

#write a program to take number from users and find the rectangle?

'''x = int(input("enter the length of rectangle :"))
print("length of rectangle ", x)

y = int(input("enter the width of rectangle:"))
print("width of rectangle",y)

area = x*y
print("area of rectangle",area)'''

#write a program to take number from users and find the area and perimeter of square?

'''a = int(input("enter the number :"))
print("side of square ", a)
area = a*a
print("area of square",area)

perimeter = 4*a
print ("perimeter of square",perimeter)'''

#write a program to swap two number without using third variable ?

'''x=int(input("enter first number:"))
y=int(input("enter second  number:"))
print("the value of x=",x)
print("the value of y=",y)
x = x+y
y=x - y
x=x - y
print("the value of x after swapping", x)
print("the value of y after swapping", y)'''

#example of data type?

'''a = 5
print("type of",type(a))'''


# String handling

'''str1="hello gatewayclasses"
str2="welcome"
print(str1[0:2])
#printing first two character using slice operator
print(str2[1:3])
#printing second and third character
print(str1[4])
#printing the element present at four index
print(str2[5])
#printing the element present at fifth index
print(str1*2)
#printing the string twice
print(str2*4)
#printing the string four time
print(str1+str2)
#concatenation'''

#PALINDROME

'''n= int(input("enter the n digit\n"))
num = n
rev= 0
while n>0:
    d = n%10
    rev= rev *10+d
    n = n//10
    print("reverse",rev)
    if rev == num:
        print("palindrome")
    else:
        print("not a palindrome")'''

#armstrong
'''n= int(input("enter the n digit\n"))
num = n
sum= 0
while n>0:
    d = n%10
    sum= sum +(d*d*d) 
    n = n//10
    print("sum",sum)
    if sum == num:
        print("armstrong")
    else:
        print("not a armstrong")'''

# factorial number

'''num = int(input("enter the factorial number\n"))
factorial =  1
if num<0:
    print("sorry , factorial does not exit in negative number")
elif num == 0:
    print ("factorial 1 is 0")
else:
    for i in range(1,num+1):
        factorial= factorial*i
        print ("the factorial is " , num , "is",factorial)'''

# favonacci
'''nterms = int(input("enter the fobonacci term:"))
n1 =0
n2 =1
count = 0
if nterms<=0:
    print("fabonacci is not sequence in negative terms")
elif nterms ==1:
    print("the fabonacci sequnce upto",nterms,":")
elif nterms ==2:
    print("the fabonacci sequence up",nterms,":")
    print(n1)
    print(n2)

else:
    print("the fabonacci sequence",":")
    print(n1)
    print(n2)
    for i in range(3,nterms+1):
        nth = n1+n2
        print(nth)

        n1=n2
        n2 =nth'''

#pattern

'''rows = int (input(" enter the number :"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*", end = " " )
    print("\n")'''

'''rows = int (input(" enter the number :"))

k = 0

for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end = " " )

        while k!= (2*i-1):
            print("*",end = " ")
            k += 1
        k=0
        print()'''

#FILE AS ANN INPUT .TXT FOR EVEN AND ODD

'''file = open("input.txt","w")
file.write("23\n")
file.write("26\n")
file.write("28\n")
file.write("13\n")
file.write("53\n")
file.close()
file1 = open("input.txt","r")
for i in file1:
    if i.strip:
        num = int(i)
        if(num%2==0):
            even = open ("even.txt","a")
            even.write(str(num))
            even.write("\n")
        else:
            odd = open ("odd.txt","a")
            odd.write(str(num))
            odd.write("\n")'''

# alpha value put in file based ?

'''file = open ("iput.txt","w")
file.close()
letters = 0
digits = 0

for a in file:
    if a.isalpha():
        letters = letters+1
    else:
        digits = digits +1'''


#NUM FUNCTION PROGRAM

import numpy  as np
x = np.arr([[2,4,6],[6,8,10]],np.int32)
print(type(x))
print(x.shape)
print(x.dtype)












         






















