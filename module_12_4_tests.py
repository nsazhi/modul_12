import logging
import unittest
from rt_with_exceptions import *


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Turtle', -5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)

        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(2)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)

        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()
