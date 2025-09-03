class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} Age: {self.age} is created")

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
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"_Name: {self._name}, _Age: {self._age}")



def main():
    person = Person("John", 20)
    
    print("\n=== 访问 _name (直接属性) ===")
    print(f"person._name = {person._name}")
    
    print("\n=== 访问 name (属性方法) ===")
    print(f"person.name = {person.name}")
    
    print("\n=== 修改 _name (直接赋值) ===")
    person._name = "Alice"
    print(f"修改后 person._name = {person._name}")
    
    print("\n=== 修改 name (调用setter) ===")
    person.name = "Bob"
    print(f"修改后 person.name = {person.name}")

    
if __name__ == "__main__":
    main()