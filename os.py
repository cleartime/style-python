# coding = utf-8

import os

if os.getuid() == 0:
    pass
else:
    print '当前用户不是root用户，请以root用户执行脚本'
    sys.exit(1)
