class student:
    grade = 10
    name = "Penguin"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.grade)
        print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()

