import unittest
from src.utils import info

class TestProject(unittest.TestCase):
    def test_info(self):
        self.assertTrue(len(info()) > 0)

if __name__ == "__main__":
    unittest.main()
