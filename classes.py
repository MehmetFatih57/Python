class Student:
    #attribute , property , field
    name = 'Mehmet Fatih'
    age = 29

    def __init__(self) -> None:
        self.name
        self.age
        print("Yapici blok calisti")

def study(self):
        print(f"{self.name}is Studying...")

student1 = Student()
student1.age = 25
student1.name = "Fatih"
student1.study()        

student2 = Student()
student2.age = 25
student2.name = "Murat"
student2.study()  