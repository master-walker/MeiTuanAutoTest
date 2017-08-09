#!/usr/bin/env python
#coding=utf8

import ConfigParser
import sys,os

src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

class ReadConfig(object):

    def __init__(self,path='..\Config\config.ini'):

        config = ConfigParser.ConfigParser()
        #读取配置文件
        config.read(path)

        #获取desired_caps数据
        self.platformName = config.get("desired_caps", "platformName")
        self.platformVersion = config.get("desired_caps","platformVersion")
        self.deviceName = config.get("desired_caps","deviceName")
        self.appPackage = config.get("desired_caps","appPackage")
        self.appActivity = config.get("desired_caps","appActivity")
        self.command_executor = config.get("desired_caps","command_executor")

        #driver wait time
        self.waitTime=config.get("driver","waitTime")

        #loginData
        self.username = config.get("login_data","username")
        self.password = config.get("login_data","password")


if __name__ != "__main__":
    ReadConfig = ReadConfig()
