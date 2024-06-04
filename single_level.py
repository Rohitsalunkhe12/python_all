class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stop..")

class Toyotacar(car):
    def __init__(self,brand):
        self.brand = brand

car1 = Toyotacar("fortuner")
car2 = Toyotacar("verna")



class fortuner(Toyotacar):
    def __init__(self,type):
        self.type = type

car1 =fortuner("diesel")

print(car1.type) 
print(car1.start())