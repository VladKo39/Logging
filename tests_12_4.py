import logging
import unittest
from rt_with_exceptions import Runner

dateformat='%Y-%m-%d %H:%M:%S'

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s || %(levelname)s || %(message)s',
                    datefmt=dateformat)

TestCase = unittest.TestCase


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            wolker = Runner('Тихоня',-4)
            for i in range(10):
                wolker.walk()
            self.assertEqual(wolker.distance, 50,
                             'test_walk: Test is filed!')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(True)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100, 'test_run: Test is filed!')

        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)



if __name__ == '__main__':
    unittest.main()
