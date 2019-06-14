#coding:utf_8
import unittest
import os
#from common import HTMLTestRunner_cn
import HTMLTestRunner

# 查找用例的文件夹 绝对路径

# 代码里面所有涉及到路径的地方都不要写死，不利于移植
#start_dir = r"E:\apiproject\case"   # 加r的意思是不去转义反斜杠“\”，或则不用r 用两个反斜杠也行：E:\\apiproject\\case

# 解决路径写死的方法，引入os模块，调用里面的方法
curpath = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件夹的路径
print(curpath)
casepath = os.path.join(curpath, "case")  # 获取当前文件夹中的case文件夹路径，以获取待执行目录
print(casepath)

pattern = "test*.py"  # .defaultTestLoader.discover()的括号里面有pattern 参数，匹配的py用例，只会执行开头名称一致的.py
# discover 加载测试用例：
discover = unittest.defaultTestLoader.discover(start_dir=casepath, pattern=pattern)
# start_dir待执行用例目录，pattern 匹配脚本用例规则，"test*.py"意思是匹配test开头的所有脚本
print(discover)

# 运行用例：
# discover 加载到的用例是一个list集合，需要重新写入到一个list对象testcase里，这样就可以用unittest里面的TextTestRunner这里类的run方法去执行。
# runner = unittest.TextTestRunner()  # 意思是返回text的文本测试结果，返回实例
# runner.run(discover) # 运行所有discover中匹配的用例

# 生成html报告：
#（由于unittest里面不能生成HTML格式，所以在写代码之前，需手动导入一个第三方模块：HTMLTestRunner）
reportpath = os.path.join(curpath, "report","report.html")  # 在获取到的curpath当前路径中，找为report的文件夹，放置report.html文件

fp = open(reportpath,"wb")  # 打开reportpath路径下的文件，用二进制写入用例执行结果报告
# 运行器
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,   # 测试报告写入文件的存储区域
                                          title="接口测试报告",  # 测试报告主题
                                          description="测试用例详情描述",  # 测试报告的描述
                                          verbosity=2)  # 冗长修改为2，默认值是1。
runner.run(discover)
fp.close()

# 将生成的测试报告发送到自己的邮箱,看接口视频12课，后半段里面有

