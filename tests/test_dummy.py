import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        # weekday = calculate(2001, 1, 3)
        # self.assertEqual(weekday, 2005)

        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2)

        weekday = calculate(2000, 2, 29)
        self.assertEqual(weekday, 1)

        weekday = calculate(2000, 3, 1)
        self.assertEqual(weekday, 2)

        weekday = calculate(2001, 2, 29)
        self.assertEqual(weekday, None)

        weekday = calculate(2001, 3, 1)
        self.assertEqual(weekday, 3)

        weekday = calculate(2004, 2, 29)
        self.assertEqual(weekday, 6)

        weekday = calculate(2004, 3, 1)
        self.assertEqual(weekday, 0)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        # retcode = main(("--jahre", "2001", "--month", "1", "--day", "3"))
        # self.assertNotEqual(retcode, 0)

        retcode = main(("--month", "1", "--day", "3", "--year", "2001"))
        self.assertEqual(retcode, 0)

        retcode = main(("--year", "2001", "--month", "2", "--day", "30"))
        self.assertNotEqual(retcode, 0)

        # retcode = main(("--year", "2001", "--month", "trzy", "--day", "30"))
        # self.assertNotEqual(retcode, 0)

        # retcode = main(("--year", "2001", "--day", "30"))
        # self.assertNotEqual(retcode, 0)

        retcode = main(("--year", "-2001", "--month", "1", "--day", "3"))
        self.assertNotEqual(retcode, 0)


if __name__ == '__main__':
    unittest.main()
