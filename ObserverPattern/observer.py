class Observer(object):

    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"{self.name} is notified with message {message}")


class Group(object):
    def __init__(self, members):
        self.members = members

    def registerGroup(self, observer):
        self.members.append(observer)

    def deRegisterGroup(self, name):
        res = None
        for idx, ele in enumerate(self.members):
            if ele.name == name:
                res = idx
        if res:
            self.members.pop(res)

    def setState(self, x):
        self.x = x
        self.__notifyAllMembers()

    def __notifyAllMembers(self):
        for member in self.members:
            member.notify(f"value of x changed to {self.x}")


if __name__ == "__main__":
    group = Group(members=[Observer("s1"), Observer("s2"), Observer("s3"), Observer("s4"), Observer("s5")])
    group.setState(10)
    group.deRegisterGroup("s4")

    group.setState(17)