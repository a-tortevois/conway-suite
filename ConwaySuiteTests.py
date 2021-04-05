import unittest
from ConwaySuite import ConwaySuite


class ConwaySuiteTests(unittest.TestCase):

    def expectConwaySuite(self, line, deep, *execptedLines):
        res = ConwaySuite().draw(line, deep)
        return self.assertEqual(res, '\n'.join((line,) + execptedLines[0:]))

    def test_01(self):
        self.expectConwaySuite('1', 1, '1 1')

    def test_02(self):
        self.expectConwaySuite('2', 1, '1 2')

    def test_03(self):
        self.expectConwaySuite('2 2', 1, '2 2')

    def test_04(self):
        self.expectConwaySuite('2 1', 1, '1 2 1 1')

    def test_05(self):
        self.expectConwaySuite('2 1 3', 1, '1 2 1 1 1 3')

    def test_06(self):
        self.expectConwaySuite('2 1 1 1', 1, '1 2 3 1')

    def test_07(self):
        self.expectConwaySuite('2 3 3 1', 1, '1 2 2 3 1 1')

    def test_08(self):
        self.expectConwaySuite('1', 2, '1 1', '2 1')

    def test_09(self):
        self.expectConwaySuite('1', 3, '1 1', '2 1', '1 2 1 1')

    def test_10(self):
        self.expectConwaySuite('1 2 1 1', 3, '1 1 1 2 2 1', '3 1 2 2 1 1', '1 3 1 1 2 2 2 1')


if __name__ == '__main__':
    unittest.main()
