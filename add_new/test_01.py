# 参数关联
# 一.参数
# 1.格式化输出

######字符串传参#########
# 用%s代替一个参数S是字符串str的意思,%d表示代替的是int类型的参数
a = "10"
b = 20
print(int(a)+b)
print(a+str(b))
c = "小王"
print("my name is %s and my age is %d years old!" % (c, b))

# 用format这种方法也可以
# {} 不设置指定位置，按默认顺序
print("my name is {} and my age is {} years old!".format(c, b))
# {} 设置指定位置
print("my name is {1} and my age is {0} years old!".format(c, b))

#####字典传参数############

b = 20
name = "老王"
token = "asxxxxxxxx"
aaa = {
    "b":b,
    "name" : name,  # 直接用参数代替，注意参数是没有用引号的
    "c": "my name is %s" %name,  # 参数是某个字符串的一半，就用%s代替
    "d": [1,2,3,b],
    "token":token
}
print(aaa)

