## coding:utf8

import os
import sys

if os.getuid() == 0:
    print '你是root用户了，但是里面还是什么都没有，嘻嘻！！'
else:
    print '你不是root用户啊，你得换他来'
    sys.exit(1)
