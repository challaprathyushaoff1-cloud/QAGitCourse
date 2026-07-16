#Practise
from dataclasses import replace
import math
import math


name ="Prathyusha"
print(type(name))
age = 25
print(type(age))
print ("Your age is:" +str(age)) 
age = age + 5
age = str(age)
print ("Your age after 5 years is:" +age)

#joining
first_name =  "Prathyusha"
last_name = "Reddy"
full_name = first_name + " " + last_name    
print("Full name is:" +full_name)

#f-strings
name = "Prathyusha"
age = 25
print(f"My name is {name} and I am {age} years old.")

print(f"2+3= {2+3} ")

#splitting
stamp = "2023-06-15 10:30:00"
date, time = stamp.split(" ")
print("Date:", date)
print("Time:", time)
print("Year:", date.split("-")[0])
print("Month:", date.split("-")[1])
print("Day:", date.split("-")[2])
print("Hour:", time.split(":")[0])
print("Minute:", time.split(":")[1])
print("Second:", time.split(":")[2])

#Repeating
print("Hello " * 3)

#indexing and slicing
text = "Hello, Automation Engineer!"
#extracting the first character
print("First character:", text[0])
#extracting the last character  
print("Last character:", text[-1])
print("First 5 characters:", text[:5])
print("Characters from index 7 to 15:", text[7:16])

date  = "2023-06-15"
year = date[:4]
month = date[5:7]
day = date[8:10]    
print("Year:", year)
print("Month:", month)
print("Day:", day)

#whitespace removal
text = "   Hello, Automation Engineer!   "  
print("Original text:", text)
print("Text after removing leading whitespace:", text.lstrip())
print("Text after removing trailing whitespace:", text.rstrip())
print("Text after removing both leading and trailing whitespace:", text.strip()) 
print("Length of the original text:",  len(text))
print("Length of the text after removing whitespace:", len(text.strip()))

#Case conversion
text = "Hello, Automation Engineer!"
task = "python programming"
print("Original text:", text)
print("Text in uppercase:", text.upper())
print("Text in lowercase:", text.lower())
print("Text in title case:", text.title())
print("Text in swapcase:", text.swapcase())
print("Text in capitalized case:", text.capitalize())
print("Text in casefold:", text.casefold())
print("Text in isupper:", text.isupper())
print("Text in islower:", text.islower())
print("Text in istitle:", text.istitle())
print(text==text.upper())

#searching and replacing
text = "Hello, Automation Engineer!"    
print("Original text:", text)
print("Index of 'Automation':", text.find("Automation"))

#Number Types
x=2
y=3.3
z= 2+3j
print(type(x))
print(type(y))
print(type(z))
print("Integer:", x)
print("Float:", y)  
print("Complex:", z)

#Number Operations
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)   
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Absolute value of -10:", abs(-10))

#Rounding
x = 3.14159
print("Original number:", x)
print("Rounded to 2 decimal places:", round(x, 2))
price = 19.99
print("Original price:", price) 
print("Rounded price:", round(price))
print("Floor of price:", math.floor(price))  # Returns 3
print("Ceil of price:", math.ceil(price))   # Returns 4
print("Square root of 16:", math.sqrt(16))  # Returns 4.0
print("Trunc of 2.3:", math.trunc(2.3))    # Returns 2

#Random Numbers

import random
random_number = random.randint(1, 100)  # Generates a random integer between