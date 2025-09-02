# Car class
class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return (self.__model + " " + self.__registration_number + " " + (str)(self.__year))

# Service class

class Service:
    def __init__(self,car_list):
        self.__car_list = car_list

    def get_car_list(self):
        return self.__car_list

    def find_cars_by_year(self,year):
        result=[]

        for car in self.__car_list:
            if car.get_year()==year:
                result.append(car.get_model())

        if not result:
            return None

        return result

    def add_cars(self, new_car_list):
        for car in new_car_list:
            self.__car_list.append(car)

    def remove_cars_from_karnataka(self):
        new_list = []
        for car in self.__car_list:
            if not car.get_registration_number().startswith("KA"):
                new_list.append(car)

        self.__car_list = new_list


car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]

# Create Service object
service = Service(car_list)

# Test find_cars_by_year
print("Cars from year 2013:", service.find_cars_by_year(2013))

# Test remove_cars_from_karnataka
service.remove_cars_from_karnataka()
print("\nCar list after removing Karnataka cars:")
for car in service.get_car_list():
    print(car)
