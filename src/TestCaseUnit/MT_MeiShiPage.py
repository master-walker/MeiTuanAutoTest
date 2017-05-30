#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月28日

@author: Master SkyWalker
'''
from ComLib import BasePage
from Elements.BaseElements import MeiShiPage

#美食页面
class MT_MeiShiPage(BasePage.BasePage):
    
    #选择餐馆
    def chooseRestaurant(self):
        self.click(MeiShiPage.resTextView)
    