# OOP

class Car:
    # color = 'White'
    # model = 'Audi'

    # Constructor
    def __init__(self, color="white", model="audi"):
        self.color = color
        self.model = model

    # Destructor
    # def __del__(self, instance):
    #     pass

    def start_engine(self) -> None:
        print('Start Engine')

    def move(self) -> None:
        print('Move')

    def move_forward(self) -> None:
        print(f'Move Forward, My car is {self.color} color')

    def move_back(self, speed=20):
        print(f"Moving backward = {speed}")


audi_RSQ8 = Car('Silver', 'RSQ8')
audi_RSQ8.color = "Silver"
audi_RSQ8.capacity_engine = 3.0

if __name__ == "__main__":
    print(audi_RSQ8.color)
    print(audi_RSQ8.capacity_engine)

    audi_RSQ8.start_engine()
    audi_RSQ8.move()
    audi_RSQ8.move_forward()
    audi_RSQ8.move_back(30)
