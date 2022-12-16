import unittest

from todoapp.Utils.Days import Day


class TestClass(unittest.TestCase):

    def test_Day_Utils_Current_Day(self):
        day = Day
        result = day.Today.name
        self.assertEqual(result, "Today")

    def test_Day_Utils_Yesterday(self):
        day = Day
        result = day.Yesterday.name
        self.assertEqual(result, "Yesterday")

