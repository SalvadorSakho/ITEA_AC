from random import randint

from Salvador_Sakho.l_8_software_engineering.Creational.abstract_entity. \
    Robot import Robot


class RobotSoldier(Robot):
    def __init__(self, number=None, supplies=None, speed=None):
        self._number = number if number is not None else randint(1, 100)
        self._bullets = supplies if supplies is not None else 100
        self._speed = speed if speed is not None else 100

    def _shoot(self, quantity=0):
        self._bullets -= quantity
        if self._bullets < 0:
            self._bullets = 0
        while quantity > 0:
            print('Tra-ta-ta')
            quantity -= 1
        return self._bullets

    def check_the_supplies(self, check_value_of):
        {
            'number': lambda: print(f'My number is:{self._number}'),
            'bullets': lambda: print(f'Bullets left: {self._bullets}'),
            'speed': lambda: print(f'My speed is: {self._speed}')
        }[check_value_of]()


class RobotBuilder(Robot):
    def __init__(self, number=None, supplies=None, speed=None):
        self._number = number if number is not None else randint(1, 100)
        self._materials = supplies if supplies is not None else 100
        self._speed = speed if speed is not None else 10

    def _build(self, what_to_build):
        self._materials = {
            "car": lambda: self._materials - 40,
            "house": lambda: self._materials - 50,
            "furniture": lambda: self._materials - 30
        }[what_to_build]()
        return self._materials

    def check_the_supplies(self, check_value_of):
        return {
            'number': lambda: print(f'My number is:{self._number}'),
            'materials': lambda: print(f'Materials left: {self._materials}'),
            'speed': lambda: print(f'My speed is: {self._speed}')
        }[check_value_of]()


class NewRobot(Robot):
    def check_the_supplies(self, check_value_of):
        return {
            'number': lambda: print(f'My number is:{self._number}'),
            'bullets': lambda: print(f'Bullets left: {self._bullets}'),
            'materials': lambda: print(f'Materials left: {self._materials}'),
            'speed': lambda: print(f'My speed is: {self._speed}')
        }[check_value_of]()

    def __init__(self, number=None, bullets=None, materials=None, speed=None):
        self._number = number if number is not None else randint(1, 100)
        self._bullets = bullets if bullets is not None else 100
        self._materials = materials if materials is not None else 100
        self._speed = speed if speed is not None else 200
