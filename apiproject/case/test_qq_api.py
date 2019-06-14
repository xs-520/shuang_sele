#coding:utf-8
import unittest
import requests
class TestQQ(unittest.TestCase):
    """ceshiQQjiekoude"""
    def test_qq_01(self):
        url = "http://japi.juhe.cn/qqevaluate/qq"
        par = {
            "key": "XXX",
            "qq": "1018812993"
        }
        r = requests.get(url, params=par)
        res = r.json()
        # 打印结果
        print(res)  #json转字典了

        # 所有的测试结果判断都可以用True和False来判断
        # 实际结果 代码运行后的结果
        shiji = res["reason"]
        #期望结果  还没有运行代码之前，脑袋里期望的结果
        qiwang = 'KEY ERROR!'
        # 断言判断  实际结果 和 期望结果
        self.assertTrue(shiji == qiwang)

        # 另一个检查点
        shiji2 = res["resultcode"]
        self.assertTrue(shiji2 == "101")
    def test_02(self):
        url = "http://japi.juhe.cn/qqevaluate/qq"
        par = {
            "key": "XXX",
            "qq": "1018812993"
        }
        r = requests.get(url, params=par)
        res = r.json()
        print(res)  #json转字典了
        shiji = res["reason"]
        shiji2 = res["resultcode"]
        self.assertTrue(shiji == 'KEY ERROR1!' or shiji2 == "101")

    def test_03(self):
        ''' QQ号错误的时候 '''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        par = {
            "key": "XXX",
            "qq": "101SSS"
        }
        r = requests.get(url, params=par)
        res = r.json()
        print(res)  #json转字典了
        shiji = res["reason"]
        shiji2 = res["resultcode"]
        self.assertTrue(shiji == 'KEY ERROR1!' or shiji2 == "101")

if __name__ == "__main__":
        unittest.main()
