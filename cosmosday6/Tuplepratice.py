#1. Create & Print
number =  (1, 2, 3, 4, 5, 6, )
print(number)

#2 Access Elements
print(number[0])
print(number[-1]) 

#unpack tuple
person = ("cosmos",17,"Kathmandu")
name, age, city = person

#4 combine tuple
a = (4, 6)
b = (1, 2, 3, 4)

#Immutability Error 
number[0] = 10
#TypeErrors: 'tuple' object does not....