# person class
# with a name attribute
# with a talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("Won Lee")
john.talk()
# print(john.name)

myOtherFriend = Person("My other friend")
myOtherFriend.talk()