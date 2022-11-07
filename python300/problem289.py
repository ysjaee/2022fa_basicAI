class Parent:
    def 호출(self):
        print("부모생성")

class Child(Parent):
    def 호출(self):
        print("자식생성")


나 = Child()
나.호출()