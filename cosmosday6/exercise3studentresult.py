class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        return f"this is about student marks {self.name}"
    def result(self): 
     if self.marks > 20:
       return "pass"
     else:
      return "fail"
s1 = Student("Ram", 23)
s1 = Student("Sita", 2)    
s3 = Student("Gita", 20)