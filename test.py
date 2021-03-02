

# 迭代器
def my_iterator(itr_src):
    itr_src = [1, 2, 3, "5", {"a": "a_value"}]
    my_iter = iter(itr_src)
    while True:
        try:
            print(next(my_iter))
        except StopAsyncIteration:
            print("迭代完成")
            break

# 生成器
def my_ganerator(gant_src):
    for i in gant_src:
        yield i
