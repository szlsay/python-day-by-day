'''
a.查找_替换_统计
find()  掌握
rfind() 了解
index() 了解
rindex() 了解
replace() 掌握
count()	掌握
'''

s = 'Hello World Hello World Hello Python'


# find()
def test_find():
    # find 查找
    idx = s.find('orld')
    print(idx)

    idx = s.find('orld',8,20)
    print(idx)


# test_find()

# index()
def test_index():
    idx = s.index('orld')
    print(idx)

    idx = s.index('orld',8,20)  # ValueError: substring not found

    print(idx)

# test_index()


# rfind() rindex()
def test_rfind_rindex():
    print(s.rfind('o'))
    print(s.rindex('o'))

    print(s.rfind('kk'))
    print(s.rindex('kk'))

print(len(s))
# test_rfind_rindex()


# replace() 替换
def test_replace():
    # 替换 时默认替换 所有的符合的子串
    print(s.replace('l','L'))
    print(s)

    # 最后听参数三表示替换个数
    print(s.replace('l','L',3))



test_replace()


# count　计数统计

def test_count():
    print(s.count('o'))
    print(s.count('o',1,5))


test_count()

print(f'a{0:5}b')





