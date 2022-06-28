import abc
from abc import ABCMeta


class Burger(metaclass=ABCMeta):
    @abc.abstractmethod
    def getDescription(self):
        pass

    @abc.abstractmethod
    def getCost(self):
        pass


class TandooriBurger(Burger):
    def getDescription(self):
        return f"TandooriBurger object"

    def getCost(self):
        return 180


class ZingerBurger(Burger):
    def getDescription(self):
        return f"ZingerBurger object"

    def getCost(self):
        return 190


class BurgerAddons(metaclass=ABCMeta):
    @abc.abstractmethod
    def getDescription(self):
        pass

    @abc.abstractmethod
    def getCost(self):
        pass


class ExtraCheeseBurger(BurgerAddons):

    def __init__(self, burger):
        self.burger = burger
        self.cheeseCost = 20

    def getDescription(self):
        return f"extra cheese"

    def getCost(self):
        return self.burger.getCost() + self.cheeseCost


class ExtraMayoBurger(BurgerAddons):

    def __init__(self, burger):
        self.burger = burger
        self.mayoCost = 40

    def getDescription(self):
        return f"extra mayo"

    def getCost(self):
        return self.burger.getCost() + self.mayoCost


class ExtraCheeseMayoBurger(BurgerAddons):

    def __init__(self, burger):
        self.burger = burger
        self.mayoCost = 40
        self.cheeseCost = 20

    def getDescription(self):
        return f"extra cheese may"

    def getCost(self):
        return self.burger.getCost() + self.mayoCost + self.cheeseCost


if __name__ == "__main__":
    tandooriBurger = TandooriBurger()
    extraCheeseBurger = ExtraCheeseBurger(burger=tandooriBurger)
    extraMayoBurger = ExtraMayoBurger(burger=tandooriBurger)
    extraCheeseMayoBurger = ExtraCheeseMayoBurger(burger=tandooriBurger)

    print(extraCheeseBurger.getCost())
    print(extraMayoBurger.getCost())
    print(extraCheeseMayoBurger.getCost())
