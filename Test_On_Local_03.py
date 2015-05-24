'''
使用系统库的范例
同时涉及列表类
'''

import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

'''
知识点：
1、引用sys模块；
2、遍历sys.argv；
3、输出sys.path列表型变量；
'''
