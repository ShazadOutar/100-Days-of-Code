class Car:
    # initialize function
    def __init__(self, seats):
        # can take input parameters
        self.seats = seats
        # but can also set some values
        self.seatbelts = True

    # make a method to change the number of seats
    def set_2_doors(self):
        self.seats = 2

    def change_num_doors(self, new_door_count):
        self.seats = new_door_count

    def copy_num_doors(self, car):
        # give yourself the same number of doors as another car
        self.seats = car.seats

    def swap_num_doors(self, car):
        # swap the value of seats attribute between 2 objects of class Car
        temp = car.seats
        car.seats = self.seats
        self.seats = temp


Nissan = Car(5)
Toyota = Car(10)
print(Nissan.seats)
print(Nissan.seatbelts)
Nissan.set_2_doors()
print(Nissan.seats)
Nissan.change_num_doors(4)
print(Nissan.seats)
Nissan.copy_num_doors(Toyota)
print(Nissan.seats)
Toyota.change_num_doors(12)
Nissan.swap_num_doors(Toyota)
print(f"Nissan seats are:{Nissan.seats}")
print(f"Toyota seats are:{Toyota.seats}")