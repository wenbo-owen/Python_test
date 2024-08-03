from my_info import *
from introduce import *

#导入模块中具有相同的变量和函数，后导入的会将先前导入的进行覆盖
#info()

#如果不想覆盖

import my_info
import introduce

my_info.info()
introduce.info()

