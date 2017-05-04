import unittest

from pybles2 import pyble
from pybles2.src import exceptions


class TestPyble(unittest.TestCase):

    def setUp(self):
        self.pb = pyble.Pyble()

    def test_title(self):
        self.pb.set_title("this is a title")
        self.assertEqual(self.pb.get_title(), "this is a title")

    def test_empty_columns(self):
        self.assertEqual(self.pb.get_columns(), list())

    def test_columns(self):
        self.pb.set_columns(['a', 'b'])
        self.assertEqual(self.pb.get_columns(), ['a', 'b'])

    def test_add_line(self):
        self.pb.set_columns(['a', 'b'])
        self.pb.add_line(['1', '2'])
        self.assertEqual(self.pb.get_lines(), [['1', '2']])

    def test_add_line_exceptions(self):
        self.pb.set_columns(['a', 'b'])
        self.pb.add_line(['1', '2'])
        self.assertRaises(
            exceptions.ColumnsNumberDoesNotMatch,
            self.pb.add_line,
            ['1', '2', '3']
        )

    def test_change_columns_when_lines_present(self):
        self.pb.set_columns(['a', 'b'])
        self.pb.add_line(['1', '2'])
        self.assertRaises(
            exceptions.ColumnsAlreadySet,
            self.pb.set_columns,
            ['c', 'd']
        )

    def test_columns_width(self):
        self.pb.set_columns(['columna', 'columnb'])
        self.pb.add_line(['1234234234', '234'])
        self.pb.add_line(['1', '234234234234'])
        self.assertEqual(self.pb.get_columns_width(), {0: 14, 1: 16})

    def test_title_width(self):
        self.pb.set_columns(['columna', 'columnb'])
        self.pb.add_line(['1234234234', '234'])
        self.pb.add_line(['1', '234234234234'])
        self.assertEqual(self.pb.get_title_width(), 30)
