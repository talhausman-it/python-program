class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
teacher = student("talha",21,2)  
print(teacher.name)      

#calling two object
class car:
    def __init__(self, brand, model, year):
        
        self.brand = brand
        self.model = model
        self.year = year
    def show(self): 
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
      


honda = car("aulto","new",2025)  
audi = car("auto","old",2024)
audi.show()
#another example of class constructer and object
class player:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        def show(self):
            print(f"Name: {self.name}, Age: {self.age}, Role: {self.role}")
            cricket= player("talha",31,"bowler")
            football = player("ali",25,"goalkeeper")
            football.show()