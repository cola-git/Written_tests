import os

# 获取项目目录路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)

# 配置文件目录的路径
CONFDIR = os.path.join(BASEDIR, "config")
print(CONFDIR)

# 日志文件目录的路径
LOGDIR = os.path.join(BASEDIR, "logs")
print(LOGDIR)

DATADIR = os.path.join(BASEDIR, "data")
