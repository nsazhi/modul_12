from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Test walk function in Runner
        :return:
        """
        runner = Runner('Turtle')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """
        Test run function in Runner
        :return:
        """
        runner = Runner('Rabbit')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """
        Test matching walk and run functions in Runner
        :return:
        """
        runner1 = Runner('Turtle')
        runner2 = Runner('Rabbit')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

    def test_fail(self):
        """
        Failed test run function in Runner
        :return:
        """
        runner = Runner('Robot')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 110)
