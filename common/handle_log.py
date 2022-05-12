import os
import logging
from common.handle_config import conf
from common.handle_path import LOGDIR


class HandleLog(object):

    @staticmethod
    def create_logger():
        # 创建收集器，设置收集器的等级
        mylog = logging.getLogger(conf.get("log", "name"))
        mylog.setLevel(conf.get("log", "ct_level"))

        # 创建输出到控制台的渠道，设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log", "sh_level"))
        mylog.addHandler(sh)

        # 创建输出到文件的渠道，设置等级
        fh = logging.FileHandler(filename=os.path.join(LOGDIR, "log.log"), encoding="utf8")
        fh.setLevel(conf.get("log", "fh_level"))
        mylog.addHandler(fh)

        # 创建日志输出格式
        formatter = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formatter)
        sh.setFormatter(fm)
        fh.setFormatter(fm)
        return mylog


log = HandleLog.create_logger()
