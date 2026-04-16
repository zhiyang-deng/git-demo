# 写一个加法函数
def add(x, y):
    return x + y

# 自动化测试：检查结果对不对
def test_add():
    result = add(2, 3)
    if result == 5:
        print("测试通过 ✅")
    else:
        print("测试失败 ❌")

# 运行测试
test_add()
print("修改正确一次")
print("修改正确2次")
print("还要修改")
print("aaa")