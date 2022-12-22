#answer 1
str="Python is a case sensitive language"

#a
print(len(str))
#b
print(str[::-1])
#c
str2=str[10:26]
print(str2)
#d
print(str.replace("a case sensitive","object oriented"))
#e
print(str.find("a"))
#f
print(str.replace(" ",""))

#answer 2
a="saira garg"
b="22103088"
c="CSE"
d="10"

print("Hey",a," Here!"
              "My SID is ",b,".I am from",c,"department. My CGPA is",d)

#answer 3
x=56
y=10
print("x & y =", x&y)
print("x | y=",x|y)
print("x ^ y=",x^y)
print("left shift both x and y with 2 bits =",x<<2,"=",y<<2)
print("right shifting x with 2 bits and y with 4 bits=", x>>2,"=",y>>4)

#answer 4
num1=float(input("enter the 1st number: "))
num2=float(input("enter the 2nd number: "))
num3=float(input("enter the 3rd number: "))
print("the greatest of all the numbers is",max(num1,num2,num3))

#answer 5
str3=input("enter the string: ")
if"name" in str3:
    print("yes")
else:
    print("no")

#answer 6
len1=float(input("enter the length of side 1:"))
len2=float(input("enter the length of side 2:"))
len3=float(input("enter the length of side 3:"))
if len1+len2>len3 and len2+len3>len1 and len1+len3>len2:
    print("yes")
else:
    print("no")