from runner_and_tournament import *
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_tournament1(self):
        self.race = Tournament(90, self.runner1, self.runner3)
        self.race_participants = list(self.race.participants)
        self.all_results['test1'] = self.race.start()

    def test_tournament2(self):
        self.race = Tournament(90, self.runner2, self.runner3)
        self.race_participants = list(self.race.participants)
        self.all_results['test2'] = self.race.start()

    def test_tournament3(self):
        self.race = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.race_participants = list(self.race.participants)
        self.all_results['test3'] = self.race.start()

    def tearDown(self):
        el = self.all_results.get(list(self.all_results.keys())[-1])
        self.assertTrue(el.get(max(key for key in el.keys())) == 'Ник')  # является ли Ник последним
        self.race_participants.sort(key=lambda p: p.speed, reverse=True)  # сортировка по скорости
        j = 0
        for i in self.race_participants:
            self.assertEqual(i.name, list(el.values())[j])  # равно ли имя из сортировки результату
            j += 1
        self.assertListEqual([], self.race.participants)  # сравнение списков: все ли добежали (просто пример)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)
