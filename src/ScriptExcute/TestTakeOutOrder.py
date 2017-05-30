#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月25日

@author: Master SkyWalker
'''

import unittest,time
from ComLib import CommonFunc,MyTest
from Config.ReadConfig import ReadConfig
from TestCaseUnit import MT_MyPage,MT_HomePage,MT_MeiShiPage,MT_TakeOutPage,MT_Restaurant,MT_SubmitOrder


class TestTakeOutOrder(MyTest.MyTest):
    
    
    def testCase(self):
        #实例化页面对象
        mt_MyPageClass=MT_MyPage.MT_MyPage(self.driver,self.logger)
        mt_HomePageClass=MT_HomePage.MT_HomePage(self.driver,self.logger)
        mt_TakeOutPageClass=MT_TakeOutPage.MT_TakeOutPage(self.driver,self.logger)
        mt_MeiShiPageClass=MT_MeiShiPage.MT_MeiShiPage(self.driver,self.logger)
        mt_RestaurantClass=MT_Restaurant.MT_Restaurant(self.driver,self.logger)
        comFuncClass=CommonFunc.CommonFunc(self.driver,self.logger)
        mt_SubmitOrderClass=MT_SubmitOrder.MT_SubmitOrder(self.driver,self.logger)
        
        #由于美团已登录账号，登录部分注释掉，进入相应的餐馆下单
        #进入我的页面，点击登录
#         mt_MyPageClass.enterLoginPage()
#         #登录账号
#         datas=[ReadConfig.username,ReadConfig.password]
#         comFuncClass.login(datas)
        
        
        time.sleep(2)
        #点击外卖，进入外卖首页
        mt_HomePageClass.enterTakeOutPage()
        #点击美食，进入餐馆列表页
        mt_TakeOutPageClass.enterMeiShiPage()
        #选择餐馆，点击
        mt_MeiShiPageClass.chooseRestaurant()
        #选择外卖
        mt_RestaurantClass.orderDishes()
        #点击结算
        comFuncClass.settleAccounts()
        #检查下单的菜品
        flag=mt_SubmitOrderClass.checkoutOrder( u"二块香辣鸡翅")
        if flag:
            self.logger.debug("选择的菜品正确")
        else:
            self.logger.debug("选择的菜品不正确")
            raise Exception
         
        #提交订单
        comFuncClass.submitOrder()
        time.sleep(3)
    
if __name__=="__main__":
    unittest.main()
