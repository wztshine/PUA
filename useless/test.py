import unittest

class TT(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.name = 'wang'
        print('!!!!!!!!!!!!!111setupclass')

    def test_name(self):
        assert self.name == 'wang'

    def test_name2(self):
        assert self.name != 'wang'

if __name__ == '__main__':
    unittest.main(verbosity=2)