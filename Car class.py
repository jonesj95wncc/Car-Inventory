# Car class
class Car:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._color = ''
        self._year = 0
        self._mileage = 0
    def add_car(self):
        try:
            self._make = input('Enter car make: ')
            self._model = input('Enter car model: ')
            self._color = input('Enter car color: ')
            self._year = int(input('Enter car year: '))
            self._mileage = int(input('Enter car mileage: '))
            return True
        except ValueError:
            print('Please enter an integer value for year and mileage')
            return False
    def __str__(self):
        return '{self._make}' '\t' '{self._model}' '\t' '{self._color}' '\t' '{self._year}' '\t' '{self._mileage}'.format(self=self)

# Update class
class Update:
    def __init__(self):
        #empty list
        self.cars = []
    def add_car(self): #add a car
        car = Car()
        if car.add_car() == True:
            self.cars.append(car)
            print ()
            print('This vehicle has been added, Thank you')
    def remove_car(self): #remove a car
        #Get the user input
            choice = int(input('Please enter the number of vehicle to be removed: '))
            update.print_inventory()
            update.cars.remove(update.cars[choice - 1])
            print ()
            print('The car has been removed')
    def print_inventory(self): #view the inventory
        car = Car()
        print('\t'.join(['','Make', 'Model','Color', 'Year', 'Mileage']))
        for idx, car in enumerate(self.cars) :
            print(idx + 1, end='\t')
            print(car)
    def edit_car(self): #edit vehicle
        car = Car() 
        #Get the user input
        choice = int(input('Please enter the number associated with the vehicle to be updated: '))
        if car.add_car() == True :
            update.cars.remove(update.cars[choice - 1])
            update.cars.insert(choice - 1, car)
            print ()
            print('The car has been updated')
    def export_inventory(self): #export inventory to file
        car = Car()
        #write a data in a file
        file = open('car_inventory.txt', 'w')
        file.write('\t'.join(['Make', 'Model','Color', 'Year', 'Mileage']))
        file.write('\n')
        for car in update.cars:
            file.write('%s\n' %car)
        file.close() #to change file access modes
        print('The car inventory has been exported to a file name car_inventory.txt')
        
#Create an object for Update class
update = Update()
#Use while True statement to keep on looping until the user exit the program
while True:
    #menu for the user
    print('****** MENU ******')
    print('1 Add a new vehicle')
    print('2 Remove a vehicle')
    print('3 View Current Inventory')
    print('4 Update Vehicle attributes')
    print('5 Export inventory into a text file')
    print('6 Quit')
    #Get the user input
    userInput=input('Please choose from the menu options: ') 
    if userInput=="1": #add a vehicle
        update.add_car()
    elif userInput=='2': #remove a vehicle
        update.remove_car()    
    elif userInput == '3': #view the inventory
        print('***Car Inventory***')
        update.print_inventory()
    elif userInput == '4': #edit a car
        update.edit_car()
    elif userInput == '5': #export inventory to file
        update.export_inventory()
    elif userInput == '6': #exit the loop
        print('Thank you!')
        break
    else:
        #invalid user input
        print('Invalid input. Please try again.')