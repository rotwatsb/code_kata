import unittest

class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        found = []
        new_str = []
        
        for c in s:
            if c in vowels:
                found.append(c)

        for i, c  in enumerate(s):
            if c in vowels:
                new_str.append(found.pop())
            else:
                new_str.append(c)
        return ''.join(new_str)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.rv = Solution()

    def test_1(self):
        self.assertEqual(self.rv.reverseVowels('Hello'), 'Holle')

    def test_2(self):
        self.assertEqual(self.rv.reverseVowels('HEap'), 'HaEp')

if __name__ == '__main__':
    unittest.main()
