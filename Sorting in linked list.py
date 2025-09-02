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
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))


class Service:
    def __init__(self, car_list):
        # Store the list of Car objects
        self.__car_list = car_list

    def get_car_list(self):
        # Return the current list of cars
        return self.__car_list

    def find_cars_by_year(self, year):
        # Create an empty list to store matching car models
        result = []

        # Loop through each car in the car list
        for car in self.__car_list:
            # Check if the car's year matches the given year
            if car.get_year() == year:
                # If it matches, add the car's model to the result list
                result.append(car.get_model())

        # If no cars matched, return None
        if not result:
            return None

        # Otherwise, return the list of matching models
        return result

    def add_cars(self, new_car_list):
        # Add new cars to the existing list
        for car in new_car_list:
            self.__car_list.append(car)

        # Sort the list by year (oldest to newest)
        self.__car_list.sort(key=lambda car: car.get_year())

    def remove_cars_from_karnataka(self):
        # Create a new list with only cars NOT from Karnataka
        new_list = []
        for car in self.__car_list:
            if not car.get_registration_number().startswith("KA"):
                new_list.append(car)

        # Replace the old list with the new filtered list
        self.__car_list = new_list


car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program