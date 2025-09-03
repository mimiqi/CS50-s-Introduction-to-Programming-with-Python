class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} {self.age} is created")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        print(f"name.setter is called")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
        print(f"age.setter is called")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        print(f"Student {self.name} {self.age} {self.subject} is created")

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject
        print(f"subject.setter is called")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}"

def main():
    person = Person("John", 20)
    print(person)
    print("\n",sep="",end="")
    student = Student("Jane", 21, "Math")
    print(student)

if __name__ == "__main__":
    main()