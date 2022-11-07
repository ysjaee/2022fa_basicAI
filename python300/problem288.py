class Parent:
    def 호출(self):
        print("부모호출")

class Child(Parent):
    def 호출(self):
        print("자식호출")


나 = Child()
나.호출()