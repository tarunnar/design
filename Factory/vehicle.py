import abc
from abc import ABCMeta


class IllegalVehicleTypeException(Exception):
    def __int__(self, message: str):
        self.message = message
        super(IllegalVehicleTypeException, self).__int__(message)


class Vehicle(metaclass=ABCMeta):
    @abc.abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def __int__(self):
        pass

    def move(self):
        print("car is moving")


class Bike(Vehicle):
    def __int__(self):
        pass

    def move(self):
        print("bike is moving")


class VehicleFactory(object):
    def __int__(self):
        pass

    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise IllegalVehicleTypeException(f"type: {vehicle_type} is illegal vehicle type")


if __name__ == "__main__":
    vehicle_factory = VehicleFactory()
    vehicle = vehicle_factory.create_vehicle("bike")
    vehicle.move()
