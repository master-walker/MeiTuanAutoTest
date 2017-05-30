#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月28日
 
'''
from ComLib import BasePage
from Elements.BaseElements import RestaurantPage

#餐馆页面
class MT_Restaurant(BasePage.BasePage):
    #点餐，勾选菜品，下单
    def orderDishes(self):
        addBtns=self.getGroupElements(RestaurantPage.addBtn)
        #点击第1个
        addBtns[0].click()
        self.logger.info("选择第一个菜品")
        

 

    