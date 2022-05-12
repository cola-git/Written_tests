import os
from configparser import ConfigParser
from common.handle_path import CONFDIR


class Config(ConfigParser):

    def __init__(self, config_name):
        super().__init__()
        self.config_name = config_name
        self.read(config_name, encoding="utf8")

    def write_data(self, section, option, value):
        self.set(section=section, option=option, value=value)
        self.write(fp=open(self.config_name, "w"))


conf = Config(os.path.join(CONFDIR, "config.ini"))
