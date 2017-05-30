#!/usr/bin/env python
#coding=utf-8

'''
Created on 2017年5月23日

@author: Master SkyWalker
'''

from ComLib import BasePage
from Elements.BaseElements import HomePage



class MT_HomePage(BasePage.BasePage):
    #进入外卖页面
    def enterTakeOutPage(self):
        self.click(HomePage.takeOutBtn)

