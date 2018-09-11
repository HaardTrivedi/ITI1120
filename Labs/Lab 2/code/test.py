import unittest
from lab2_prog_solutions import repeater, reverse, roots, real_roots

class TestStringMethods(unittest.TestCase):

    def test_repeater(self):
        self.assertEqual(repeater('AAA','x',3), '_AAAxAAAxAAAx_')
        self.assertEqual(repeater('+','--',30), '_+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--_')
        self.assertEqual(repeater('T', '|_|',100), '_T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|T|_|_')


    def test_roots(self):
        self.assertAlmostEqual(roots(-1,4,1.5), [-0.34520787991171487, 4.345207879911715], places=7, msg=None, delta=None)
        self.assertAlmostEqual(roots(1,2,1), [-1.0, -1.0], places=7, msg=None, delta=None)

    def test_real_roots(self):
        self.assertTrue(real_roots(-1,4,1.5))
        self.assertTrue(real_roots(1,2,1))
        self.assertFalse(real_roots(1,1,1))
        
    def test_reverse(self):
        self.assertEqual(reverse(72),27)
        self.assertEqual(reverse(24),42)
        self.assertEqual(reverse(12),21)


if __name__ == '__main__':
    unittest.main()
