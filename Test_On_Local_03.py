'''
使用系统库的范例
同时涉及列表类
'''

import sys,Test2

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

Test2.func(3, 7)
Test2.func(25, c=24)
Test2.func(c=50, a=100) 

'''
知识点：
1、引用sys模块；
2、遍历sys.argv；
3、输出sys.path列表型变量；
4、建立__init__.py文件
5、引用自定义的Test2模块中的func函数；
'''
