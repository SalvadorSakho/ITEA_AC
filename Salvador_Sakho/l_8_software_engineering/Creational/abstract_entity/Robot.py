from abc import ABC, abstractmethod


class Robot(ABC):
    def _go(self, distance):
        passed_distance = 0
        while distance > passed_distance:
            print('Walking...')
            if passed_distance + self._speed > distance:
                passed_distance = distance - passed_distance
                return passed_distance

            passed_distance += self._speed
        return passed_distance

    def _speak(self, command):
        print(f"I finished to {command}.")

    def _action(self, command, value):
        if command == 'go':
            self._go(value)
        elif command == 'shoot':
            self._shoot(value)
        elif command == 'build':
            self._build(value)
        return command

    def listen(self, commands):
        for command in commands:
            for key, values in command.items():
                self._speak(self._action(key, values))

    @abstractmethod
    def check_the_supplies(self, check_value_of):
        pass
