'''
startswith() 判断是否以指定字符串开头 （掌握）
endswith()   判断是否以指定字符串结束 （掌握）
isupper()	判断是不是大写字符	(理解)
islower()	判断是不是小写字符	(理解)
isdigit()	判断是不是数字字符 (理解)
isalpha()	判断是不是字母 (理解)
isalnum()	判断是不是字母或数字字符 (理解)
isspace()	判断是不是空白字符，包含空格，换行符\n，制表符\t (理解)注意''空字符串不是空白字符
'''


# startswith() 判断是否以指定字符串开头 （掌握）
def test_startswith():
    print('13800138000'.startswith('138'))
    print('18300138000'.startswith('138'))
    print('18700138000'.startswith('138'))
    print('13300138000'.startswith('138'))

# test_startswith()

# endswith()   判断是否以指定字符串结束 （掌握）

def test_endswith():
    print('www.xxxgov.com'.endswith('.gov'))
    print('www.xxx.gov'.endswith('.gov'))

# test_endswith()


def test_other():
    # print('hello'.isupper())
    # print('Hello'.isupper())
    # print('HELLO'.isupper())

    # print('hello'.islower())
    # print('Hello'.islower())
    # print('HELLO'.islower())

    # print('hello'.isalpha())
    # print('Hello'.isalpha())
    # print('HELLO'.isalpha())
    # print('123'.isalpha())
    # print('abc123'.isalpha())

    # print('HELLO'.isalnum())
    # print('123'.isalnum())
    # print('abc123'.isalnum())
    # print('abc 123'.isalnum())

    # print('HELLO'.isdigit())
    # print('123'.isdigit())
    # print('abc123'.isdigit())
    # print('123abc'.isdigit())

    print(''.isspace())
    print(' '.isspace())
    print('\t'.isspace())
    print('\n'.isspace())





test_other()