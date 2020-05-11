from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_robot(self, robot, number=None, supplies=None, speed=None):
        pass

    @abstractmethod
    def add_new_model(self, robot):
        pass
