#!/usr/bin/env python
#coding=utf-8

'''
Created on 2017年5月30日

页面常用的公共方法
'''
import time
from ComLib import BasePage
from Element.Elements import LoginPage,CommonElsPage


class CommonPage(BasePage.BasePage):
    
    #登录方法
    def login(self,datas):
        t1=time.time()
        logger=self.logger
        logger.info("\n---------------------------------------------------------------------------")
        #提交数据，登录
        self.submitData(LoginPage.loginElements, datas)
        logger.info("enter loginPage  Spend {0} seconds".format(time.time()-t1))
        
    #外卖结算
    def settleAccounts(self):
        self.click(CommonElsPage.accountBtn)
        
    #提交订单
    def submitOrder(self):
        self.click(CommonElsPage.submitBtn)
        self.logger.info("提交订单成功")
     
      
