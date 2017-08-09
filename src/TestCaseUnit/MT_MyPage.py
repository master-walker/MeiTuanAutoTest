#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月25日

@author: Master SkyWalker
'''
from Element.Elements import MyPage
from ComLib import BasePage


class MT_MyPage(BasePage.BasePage):
    
    #进入登录页面
    def enterLoginPage(self):
        self.click(MyPage.myBtn)
        self.click(MyPage.clickLoginBtn)