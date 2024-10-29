from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: ([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]], 3), 
            2: ([[3,2,4],[2,1,9],[1,1,7]], 0),
            3: ([[102,168,168,86,228],[209,210,182,153,55],
                 [99,76,168,40,262],[260,257,227,97,153],
                 [189,280,257,239,93],[300,108,68,220,76]], 2),
            4: ([[65,200,263,220,91,183,2,187,175,61,225,120,39],
                 [111,242,294,31,241,90,145,25,262,214,145,71,294],
                 [152,25,240,69,279,238,222,9,137,277,8,143,143],
                 [189,31,86,250,20,63,188,209,75,22,127,272,110],
                 [122,94,298,25,90,169,68,3,208,274,202,135,275],
                 [205,20,171,90,70,272,280,138,142,151,80,122,130],
                 [284,272,271,269,265,134,185,243,247,50,283,20,232],
                 [266,236,265,234,249,62,98,130,122,226,285,168,204],
                 [231,24,256,101,142,28,268,82,111,63,115,13,144],
                 [277,277,31,144,49,132,28,138,133,29,286,45,93],
                 [163,96,25,9,3,159,148,59,25,81,233,127,12],
                 [127,38,31,209,300,256,15,43,74,64,73,141,200]], 3)
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

    @timeout(0.5)
    def test_Case3(self):
        grid, output = self.testCases[3]
        result = self.obj.maxMoves(grid = grid)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case4(self):
        grid, output = self.testCases[4]
        result = self.obj.maxMoves(grid = grid)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()