class Student:
    def init(self, name, age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı blok çalıştı")

    def study(self):
        print(f"{self.name} is studying...")

student1 = Student("Mehmet" , 25)
#student1.study()        

student2 = Student("Fatih" , 25)
#student2.study()  