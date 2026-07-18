#Boolean 
print(type(True))
print(bool(156))
print(bool("Hi"))
print(bool(0))
print(bool(""))

#comparision operators
print(5>3)
print(5<3)
print(5>=3)
print(5<=3)
print(5==3)
print(5!=3)
print(5==5)
print(5!=5)
print("a" == "b")
print(1<4<9)
#is age between 18 and 30
age = 20
print(age>18 and age<30)

#logical operators
print(5>3 and 5<10)
print(5>3 or 5<10) 
print(not(5>3 and 5<10))
#checking if a number is even or odd
x = 7
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")