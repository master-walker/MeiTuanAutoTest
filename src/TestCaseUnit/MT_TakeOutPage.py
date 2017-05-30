#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月28日

'''
from ComLib import BasePage
from Elements.BaseElements import TakeOutPage

#外卖首页
class MT_TakeOutPage(BasePage.BasePage):
    #进入美食页面
    def enterMeiShiPage(self):
        self.click(TakeOutPage.meishiTextView)
    