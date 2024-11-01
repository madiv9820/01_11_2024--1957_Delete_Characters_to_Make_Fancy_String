from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {1: ("leeetcode", "leetcode"), 2: ("aaabaaaa", "aabaa"), 3: ("aab", "aab")}
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, output = self.testCases[1]
        result = self.obj.makeFancyString(s = s)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.testCases[2]
        result = self.obj.makeFancyString(s = s)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        s, output = self.testCases[3]
        result = self.obj.makeFancyString(s = s)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()