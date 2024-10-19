import unittest
import module_12_3_tests

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3_tests.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3_tests.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTS)
