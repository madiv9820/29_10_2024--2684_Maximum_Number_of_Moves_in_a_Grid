from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: ([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]], 3), 
            2: ([[3,2,4],[2,1,9],[1,1,7]], 0)
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        grid, output = self.testCases[1]
        result = self.obj.maxMoves(grid = grid)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        grid, output = self.testCases[2]
        result = self.obj.maxMoves(grid = grid)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()