#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月28日

'''
from selenium.webdriver.common.by import By
from ComLib import BasePage,Public

#下单页面
class MT_SubmitOrder(BasePage.BasePage):
    
    
    def checkoutOrder(self,checkText):
        locate="//android.widget.TextView[contains(@text,'"+checkText+"')]"
        locators=(By.XPATH,locate)
        elementText=self.getElementText(locators)
        return Public.is_text_present(elementText, checkText)