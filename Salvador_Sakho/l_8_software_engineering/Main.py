from Salvador_Sakho.l_8_software_engineering.Behavioral.Observer\
    .Publisher import Publisher
from Salvador_Sakho.l_8_software_engineering.Behavioral.Observer\
    .Subscriber import Subscriber
from Salvador_Sakho.l_8_software_engineering.Creational.entity_impl \
    .Factory_impl import MilitaryRobotFactory, CivilRobotFactory
from Salvador_Sakho.l_8_software_engineering.Creational.entity_impl \
    .Robot_impl import RobotBuilder, RobotSoldier
from Salvador_Sakho.l_8_software_engineering.Structural.Adapter\
    .Adapter import Adapter


def main():
    military_factory = MilitaryRobotFactory()
    civil_factory = CivilRobotFactory()
    # publisher = Publisher([military_factory, civil_factory])
    adapter = Adapter(civil_factory, military_factory)

    robot_soldier = military_factory.create_robot(RobotSoldier)
    robot_soldie2 = military_factory.create_robot(RobotSoldier)
    robot_soldier3 = military_factory.create_robot(RobotSoldier)
    robot_builder = civil_factory.create_robot(RobotBuilder)

    robot_soldier.listen([{'shoot': 30}])
    robot_builder.listen([{'build': 'house'}])

    robot_soldier.check_the_supplies('bullets')
    robot_builder.check_the_supplies('materials')

    adapter.to_builder([robot_soldier, robot_soldie2], RobotBuilder)

    # subscriber = Subscriber(publisher)
    # print(subscriber.communicate({
    #     'command': 'subscribe',
    #     'email': 'testEmail121@gmail.com',
    #     'observable object': 'MilitaryRobotFactory'}))
    #
    # print(subscriber.communicate({
    #     'command': 'subscribe',
    #     'email': 'testEmail2@gmail.com',
    #     'observable object': 'MilitaryRobotFactory'}))
    #
    # # Фиктивно добавляем новую изготавливаемую модель.
    # military_factory.add_new_model('MilitaryDrone', publisher)
    #
    # print(subscriber.communicate({
    #     'command': 'get updates',
    #     'observable object': 'MilitaryRobotFactory',
    #     'email': 'testEmail121@gmail.com'}))
    #
    # print(subscriber.communicate({
    #     'command': 'unsubscribe',
    #     'email': 'testEmail121@gmail.com',
    #     'observable object': 'MilitaryRobotFactory'}))
    #
    # print(subscriber.communicate({
    #     'command': 'subscribe',
    #     'email': 'testEmail121@gmail.com',
    #     'observable object': 'CivilRobotFactory'}))
    #
    # print(subscriber.communicate({
    #     'command': 'get updates',
    #     'observable object': 'CivilRobotFactory',
    #     'email': 'testEmail121@gmail.com'}))
    #
    # print(subscriber.communicate({
    #     'command': 'unsubscribe',
    #     'email': 'testEmail121@gmail.com',
    #     'observable object': 'CivilRobotFactory'}))


if __name__ == '__main__':
    main()
