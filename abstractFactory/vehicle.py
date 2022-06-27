import abc
from abc import ABCMeta


class IllegalVehicleTypeException(Exception):
    def __int__(self, message: str):
        self.message = message
        super(IllegalVehicleTypeException, self).__int__(message)


class IllegalVehicleFactoryTypeException(Exception):
    def __int__(self, message: str):
        self.message = message
        super(IllegalVehicleFactoryTypeException, self).__int__(message)


class Vehicle(metaclass=ABCMeta):
    @abc.abstractmethod
    def move(self):
        pass


class HyundaiBike(Vehicle):
    def move(self):
        print("hyundai bikes")


class HyundaiCars(Vehicle):
    def move(self):
        print("hyundai cars ")


class ToyotaCars(Vehicle):
    def move(self):
        print("Toyota cars is moving")


class ToyotaBikes(Vehicle):
    def move(self):
        print("Toyota bike is moving")


class VehicleFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_vehicle(self, vehicle_type):
        pass


class HyundaiFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return HyundaiCars()
        elif vehicle_type == "bike":
            return HyundaiBike()
        else:
            raise IllegalVehicleTypeException(f"type: {vehicle_type} is illegal vehicle type")


class ToyotaFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return ToyotaCars()
        elif vehicle_type == "bike":
            return ToyotaBikes()
        else:
            raise IllegalVehicleTypeException(f"type: {vehicle_type} is illegal vehicle type")


class FactoryCreator(object):
    def create_factory(self, type):
        if type == "hyundai":
            return HyundaiFactory()
        elif type == "toyota":
            return ToyotaFactory()
        raise IllegalVehicleTypeException()


if __name__ == "__main__":
    hyundaiFactory = FactoryCreator().create_factory("hyundai")
    toyotaFactory = FactoryCreator().create_factory("toyota")

    hyundaiFactory.create_vehicle("car").move()
    hyundaiFactory.create_vehicle("bike").move()

    toyotaFactory.create_vehicle("car").move()
    toyotaFactory.create_vehicle("bike").move()

