target = __import__("domain", globals={"__name__": __name__})
# sum = target.sum

import unittest

class TestSum(unittest.TestCase):
    # def test_10(self):
    #     self.assertEqual(target.x,10)

    def test_d(self):
        test = target.Domain('fixtures/tex.txt',1,2)
        self.assertEqual(test.s(), 21)


if __name__ == '__main__':
    unittest.main()