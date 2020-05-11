from collections import defaultdict


class Adapter:
    def __init__(self, civil_factory, military_factory):
        self.civil_factory = civil_factory
        self.military_factory = military_factory
        self.transformed_robots = defaultdict(list)

    def to_builder(self, robots, robot_type):
        # previously it was military robot
        # , so when it transformed it to civil
        # , it has more capacity then standard civil robot
        for robot in robots:
            self.transformed_robots['RobotBuilder'].append(
                {
                    'NewRobot': lambda: self.civil_factory.create_robot(
                        robot_type,
                        robot.__dict__['_number'],
                        {
                            'materials': robot.__dict__['materials']
                            if robot.__dict__['materials'] > 50 else 100,
                            'bullets': 0
                        },
                        20),
                    'RobotSoldier': lambda: self.civil_factory.create_robot(
                        robot_type,
                        robot.__dict__['_number'],
                        {
                            'materials': 100,
                            'bullets': 0
                        },
                        20)
                }[robot.__class__.__name__]()
            )
        return self.transformed_robots

    def to_soldier(self, robots, robot_type):
        # previously it was civil robot
        # , so when it transformed it to military
        # , it has less speed then standard military robot
        for robot in robots:
            self.transformed_robots['RobotSoldier'].append(
                {
                    'NewRobot': lambda: self.military_factory.create_robot(
                        robot_type, robot.__dict__['_number'], {
                            'materials': 0
                            , 'bullets': robot.__dict__['bullets']
                            if robot.__dict__['bullets'] > 50 else 100
                        }, 200
                    ),
                    'RobotBuilder': lambda: self.military_factory.create_robot(
                        robot_type, robot.__dict__['_number'], {
                            'materials': 0
                            , 'bullets': 100
                        }, 50
                    )
                }[robot.__class__.__name__]()
            )
        return self.transformed_robots

    def to_new_robot(self, robots, robot_type):
        # Robot new  generation
        # Hybrid of civil and military robot
        for robot in robots:
            self.transformed_robots['NewRobot'].append(
                {
                    'RobotBuilder': lambda: self.civil_factory.create_robot(
                        robot_type, robot.__dict__['_number']
                        , {
                            'materials': robot.__dict__['materials']
                            if robot.__dict__['materials'] > 50 else 150
                            , 'bullets': 100
                        }
                        , 20
                    ),
                    'RobotSoldier': lambda: self.civil_factory.create_robot(
                        robot_type, robot.__dict__['_number']
                        , {
                            'materials': 150
                            , 'bullets': robot.__dict__['bullets']
                            if robot.__dict__['bullets'] > 50 else 100
                        }
                        , 20
                    )
                }[robot.__class__.__name__]()
            )
        return self.transformed_robots
