import unittest
from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):

    def test_no_fee_within_grace_period(self):
        duck = DuckFine("M001")

        fee = duck.charge(2)

        self.assertEqual(fee, 0.00)

    def test_fee_after_grace_period(self):
        duck = DuckFine("M001")

        fee = duck.charge(3)

        self.assertEqual(fee, 0.50)

    def test_deluxe_doubles_fee(self):
        duck = DuckFine("M001")

        fee = duck.charge(4, deluxe=True)

        self.assertEqual(fee, 2.00)

    def test_fee_cannot_exceed_maximum(self):
        duck = DuckFine("M001")

        fee = duck.charge(20)

        self.assertEqual(fee, 5.00)

    def test_negative_days_late_raises_error(self):
        duck = DuckFine("M001")

        with self.assertRaises(ValueError):
            duck.charge(-1)

    def test_total_owed_accumulates_fees(self):
        duck = DuckFine("M001")

        duck.charge(3)   # $0.50
        duck.charge(4)   # $1.00

        self.assertEqual(duck.total_owed, 1.50)


if __name__ == "__main__":
    unittest.main()