#!/usr/bin/env python
#coding=utf-8
'''
所有页面对象类，存放各个页面的元素

'''
from selenium.webdriver.common.by import By

#公共元素
class CommonElementsPage(object):
    #结算按钮
    accountBtn=(By.XPATH,"//android.widget.TextView[contains(@text,'去结算')]","去结算")
    #提交提单按钮
    submitBtn=(By.XPATH,"//android.widget.LinearLayout/android.widget.TextView[contains(@text,'提交订单')]","提交订单")
    
    
#我的页面
class MyPage(object):
    myBtn=(By.XPATH,"//android.widget.LinearLayout/android.widget.TextView[contains(@text,'我的')]","我的")
    clickLoginBtn=(By.XPATH,"//android.widget.TextView[contains(@text,'请点击登录')]","请点击登录")


#登录页  
class LoginPage(object):         
    userNameInputBox=(By.ID,"com.sankuai.meituan:id/username","手机号")
    passwdInputBox=(By.ID,"com.sankuai.meituan:id/password","密码")
    loginBtn=(By.ID,"com.sankuai.meituan:id/login","登录")
    #登录页面元素
    loginElements=[userNameInputBox,passwdInputBox,loginBtn]

#首页   
class HomePage(object):
    #外卖按钮
    takeOutBtn=(By.XPATH,"//android.widget.TextView[contains(@text,'外卖')][@index=0]","外卖")

    
#外卖首页
class TakeOutPage(object):
    #美食TextView
    meishiTextView=(By.XPATH,"//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'美食')][@index=1]","美食")
    
    
#美食餐馆页面
class MeiShiPage(object):
    #餐馆TextView
    resTextView=(By.XPATH,"//android.widget.LinearLayout/android.widget.TextView[contains(@text,'肯德基')]","肯德基")
#     resTextView=(By.XPATH,"//android.widget.LinearLayout/android.widget.TextView[contains(@text,'永和大王')]","永和大王")
    
#餐馆，点餐页面
class RestaurantPage(object):
    addBtn=(By.ID,"com.sankuai.meituan:id/img_foodCount_add")

    


