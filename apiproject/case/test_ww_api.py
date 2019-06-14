#coding:utf-8
import unittest
import requests
class TestQQ(unittest.TestCase):

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