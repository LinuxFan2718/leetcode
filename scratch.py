import threading

class Vehicle(object):
  def __init__(self):
    self.x = 3

  @staticmethod
  def derp(whatever):
    return 4 + 9

class Car(Vehicle):
  def drive(self):
    print("gooooo")
  
  @classmethod
  def report(self):
    print(type(self))

  @classmethod
  def make_vehicle(cls):
    newCar = Car()
    newVehicle = cls()
    return newCar, newVehicle

d = Car()
print(d.x)
print(d.derp('derp'))
print(Car.derp('herp'))
nc, nv = d.make_vehicle()
pass