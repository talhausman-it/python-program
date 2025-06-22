class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def hello(cls):
        print("hello, how are you")

    @staticmethod
    def static():
        print("hello, I'm Talha Usman")

forest = animal("lion", 5)
forest.static()  # Now this works

#inheritance
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The name is {self.name} and age is {self.age}")

class Human(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# Creating instances
talha = Student("talha", 22)
talha.show()

student2 = Human("talha", 22, 'A')
student2.show()
print(f"Grade: {student2.grade}")
#example of inheritance one parent and child
class pakistan:
    def __init__(self, name):
        self.name= name
        print(f"welcome  {self.name}")
        def show()
class student(pakistan):
       def __init__(self, name,age):
           super().__init__(name)
                         self.age = age
              def welcome(self):

