import unittest

class Test(unittest.TestCase):
    def test_01(self):
        a = "hi"
        b = "hi"
        self.assertEqual(a, b)  # 判断a和b相等
        # self.assertNotEqual(a, b)  # 不相等

        #所有的判断都可以用assertTrue（）来进行判断
        self.assertTrue(a == b)  # 判断a和b相等
        self.assertTrue(a != b)  # 判断a和b不相等
        self.assertTrue(a not in b)  # 判断a不在b里面
        self.assertTrue(a==b and a in b)

    def test_02(self):
        a = "hi"
        b = "hi hello"
        self.assertIn(a, b)  #  判断a 包含在b 里面
        # self.assertNotIn(a, b)

    def test_03(self):
        a = "hi"
        b = "hi hello"
        self.assertTrue(a in b)  # 判断a in b为真
        # self.assertFalse()

if __name__ == "__main__":
    unittest.main()