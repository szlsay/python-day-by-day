# from . import a
# from . import b



# 也可以使用 __all__ 来指定 可以导入 的模块
# 但是这种 方式 不通用
# 只能用在 from 包名 import * 导入 所有模块的情况
# 通过这个 __all__ 可以来设置哪个模块可以被导入
__all__ = ['a','b']  # 导入了当前包中的a模块和b模块
# __all__ = ['a']   # 只导入了当前包中的a模块，b模块不会被导入