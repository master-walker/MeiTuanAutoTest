#!/usr/bin/env python
#coding=utf-8
'''

Description:公共参数配置和公共函数模块

'''
import os,sys,logging.config
from appium import webdriver
from Config.ReadConfig import ReadConfig


sys_path=os.path.abspath("..")
sys.path.append(sys_path)
reload(sys)

#获取driver
def getDriver():
    desired_caps = {}
    desired_caps['platformName'] = ReadConfig.platformName
    desired_caps['platformVersion'] = ReadConfig.platformVersion
    desired_caps['deviceName'] = ReadConfig.deviceName
    desired_caps['appPackage'] = ReadConfig.appPackage
    desired_caps['appActivity'] = ReadConfig.appActivity
    
    driver = webdriver.Remote(ReadConfig.command_executor, desired_caps)
    return driver

#获取日志记录器
def get_logger():
    logging.config.fileConfig("../Config/logConf.ini")
    logger=logging.getLogger()
    return logger  


# 判断文本是否存在页面
def is_text_present(elementText,checkText):

    if checkText in elementText:
        return True
    else:
        return False
  

        