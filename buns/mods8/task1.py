class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def __str__(self):
        return f"Transport: Coordinates={self.coordinates}, Speed={self.speed}, Brand={self.brand}, Year={self.year}, Number={self.number}"

    def isInArea(self, pos_x, pos_y, length, width):
        x, y = self.coordinates
        return pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and passengers_capacity > 0:
            self._passengers_capacity = passengers_capacity
        else:
            raise ValueError("Passengers capacity must be a positive integer.")

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and 0 <= number_of_passengers <= self.passengers_capacity:
            self._number_of_passengers = number_of_passengers
        else:
            raise ValueError("Number of passengers must be a non-negative integer not exceeding passengers capacity.")


class Cargo:
    def __init__(self, carrying):
        self._carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int) and carrying > 0:
            self._carrying = carrying
        else:
            raise ValueError("Carrying capacity must be a positive integer.")


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class Auto(Transport):
    pass


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)


class Boat(Ship):
    pass



class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)

class Airplane(Plane):
    pass


class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoPlane(Plane, Cargo):
    pass


class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)


transport = Transport((0, 0), 100, "Generic", 2022, "ABC123")
print(transport)

passenger = Passenger(50, 30)
print(passenger)

cargo = Cargo(5000)
print(cargo)

plane = Plane((0, 0), 500, "Boeing", 2020, "XYZ789", 10000)
print(plane)

auto = Auto((0, 0), 120, "Toyota", 2019, "DEF456")
print(auto)

ship = Ship((0, 0), 30, "Titanic", 1912, "SHIP001", "Southampton")
print(ship)

car = Car((0, 0), 80, "Honda", 2021, "GHI789")
print(car)

bus = Bus((0, 0), 60, "Mercedes", 2018, "BUS123", 40, 25)
print(bus)

cargo_auto = CargoAuto((0, 0), 90, "Ford", 2020, "CARGO456", 3000)
print(cargo_auto)

boat = Boat((0, 0), 25, "Fishing Boat", 2015, "BOAT789", "Harbor")
print(boat)

passenger_ship = PassengerShip((0, 0), 20, "Cruise Ship", 2010, "CRUISE001", "Port", 500, 300)
print(passenger_ship)

cargo_ship = CargoShip((0, 0), 15, "Cargo Ship", 2005, "CARGO002", "Dock", 10000)
print(cargo_ship)

airplane = Airplane((0, 0), 700, "Airbus", 2015, "AIR001", 12000)
print(airplane)

passenger_plane = PassengerPlane((0, 0), 600, "Boeing", 2018, "PASS001", 800, 150, 100)
print(passenger_plane)

cargo_plane = CargoPlane((0, 0), 650, "CargoJet", 2020, "CARGO003", 5000)
print(cargo_plane)

seaplane = Seaplane((0, 0), 300, "Amphibian", 2017, "SEA001", 500, "Seaport")
print(seaplane)
