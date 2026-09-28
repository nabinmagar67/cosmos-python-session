#1 define the furit class 
class Fruit:
    def __init__(self, name):
        self.name = name
    def describe(self):
     return f"This fruit is called {self.name}"


#2 Instantiate objects
f1 = Fruit("Apple")
f2 = Fruit("Banana")

#3 Call method and print output 
print(f1.describe())
print(f2.describe())

