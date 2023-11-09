from datetime import datetime
from data import Data
import unittest


class Tests(unittest.TestCase):
    def test_compare_dates(self):
        date_1 = datetime.now().strftime("%m/%d/%Y")
        date_2 = datetime.now().strftime("%m/%d/%Y")
        data = Data()
        self.assertTrue(data.compare_dates(date_1, date_2), "should be True")


if __name__ == "__main__":
    unittest.main()
