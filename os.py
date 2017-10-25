## coding:utf8

import os
import sys

if os.getuid() == 0:
    pass
else:
    print '你不是root用户啊，你得换他来'
    sys.exit(1)
