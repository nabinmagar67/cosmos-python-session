class Student:
    def __init__(self, name):
        self.name = name   # Attribute
    def greet(self):
        return f"Hi, I'm {self.name}"
s1 = Student("Rita")
print(s1.greet())
