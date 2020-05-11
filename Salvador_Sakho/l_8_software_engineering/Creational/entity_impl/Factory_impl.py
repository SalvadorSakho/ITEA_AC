from Salvador_Sakho.l_8_software_engineering.Creational.abstract_entity \
    .Factory import AbstractFactory
from Salvador_Sakho.l_8_software_engineering.Creational \
    .entity_impl.Robot_impl import RobotSoldier, RobotBuilder, NewRobot


class MilitaryRobotFactory(AbstractFactory):
    available_robots = []

    def __init__(self):
        self.available_robots = ['RobotSoldier']

    def create_robot(self, robot_class, number=None, supplies=None,
                     speed=None):
        value = {
            "RobotSoldier": lambda: RobotSoldier(
                number
                , supplies['bullets'] if supplies is not None else None
                , speed
            )
        }[robot_class.__name__]()
        return value

    def add_new_model(self, robot, publisher):
        self.available_robots.append(robot)
        military_factory = self
        publisher._notify_subscriber('', military_factory)


class CivilRobotFactory(AbstractFactory):
    available_robots = []

    def __init__(self):
        self.available_robots = ['RobotBuilder', 'NewRobot']

    def create_robot(self, robot_class, number=None, supplies=None,
                     speed=None):
        value = {
            "RobotBuilder": lambda: RobotBuilder(
                number
                , supplies['materials'] if supplies is not None else None
                , speed
            ),
            "NewRobot": lambda: NewRobot(
                number
                , supplies['materials'] if supplies is not None else None
                , supplies['bullets'] if supplies is not None else None
                , speed
            )
        }[robot_class.__name__]()
        return value

    def add_new_model(self, robot, publisher):
        self.available_robots.append(robot)
        civil_factory = self
        publisher._notify_subscriber('', civil_factory)
