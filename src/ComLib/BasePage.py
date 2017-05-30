#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月29日

操作页面元素的基类
'''
import time,traceback,os,sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException


src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

success = "SUCCESS   "
fail = "FAIL   "


class BasePage(object):
    
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
    
    #获取元素和元素信息，返回 数组
    def _getElements(self,locators):
        driver=self.driver
        logger=self.logger
        t1=time.time()
        try:
            elements=[]
            element=WebDriverWait(driver,10).until(EC.presence_of_element_located(locators[:2]))
            if len(locators)==3:
                elementsAndInfosTuple=(element,locators[-1])
            elif len(locators)==2:
                elementsAndInfosTuple=(element,"")
            elements.append(elementsAndInfosTuple)
            logger.info("{0} getElement {1}, Spend {2} seconds".format(success,locators[-1],time.time()-t1))
            return elements
            
        except (NoSuchElementException,TimeoutException):
            logger.info("{0} getElement {1}, Spend {2} seconds".format(fail,locators[-1],time.time()-t1))
            raise Exception
        
    #根据locators获取一个元素，或多个元素
    def getElementAndInfos(self,locators):
        logger=self.logger
        try:
            if isinstance(locators, tuple):
                elements=self._getElements(locators)
                return elements
            
            elif isinstance(locators, list):
                elements=[]
                for locate in locators:
                    elements.extend(self._getElements(locate))
                return elements
            
        except TypeError:
            logger.info("参数传值异常")
            return False
    
    
    #获取一组相同类型元素
    def getGroupElements(self,locate,num=None):
        driver=self.driver
        logger=self.logger
        t1=time.time()
        try:
            groupElements=WebDriverWait(driver,5).until(EC.presence_of_all_elements_located(locate))
            #获取指定个数的元素
            elements=groupElements[:num]
            logger.info("{0} getElement {1}, Spend {2} seconds".format(success,groupElements[-1],time.time()-t1))
            return elements
        except TimeoutException:
            logger.info("{0} getElement {1}, Spend {2} seconds".format(fail,groupElements[0],time.time()-t1))
            return False
                
    #输入数据并提交
    #默认参数值应该是不可变的
    def submitData(self,locators,datas,sleep_time=2):
        #输入数据
        self.inputData(locators[:-1], datas)
        time.sleep(sleep_time)
        #提交
        self.click(locators[-1])   
    
    #输入数据
    def inputData(self,locators,datas):
        t1=time.time()
        logger=self.logger
        try:
            elements=self.getElementAndInfos(locators)
            flag=isinstance(datas, str)
            flag1=isinstance(datas, list)
            flag2=isinstance(datas, unicode)
            for index,element in enumerate(elements):
                if flag or flag2:
                    element[0].clear()
                    element[0].send_keys(datas)
                    logger.info("{0} input {1}, Spend {2} seconds".format(element[1],datas,time.time()-t1))
                elif flag1:
                    element[0].clear()
                    element[0].send_keys(datas[index])
                    logger.info("{0} input {1}, Spend {2} seconds".format(element[1],datas[index],time.time()-t1))
                else:
                    logger.debug("inputData传值异常")
                    
        except IndexError:
            print traceback.print_exc()
            
        
          
    #点击元素
    def click(self,locators,sleep_time=2):
        elements=self.getElementAndInfos(locators)
        t1=time.time()
        logger=self.logger
        try:
            for element in elements:
                element[0].click()
                logger.info("{0} click  Spend {1} seconds".format(element[1],time.time()-t1))
                time.sleep(sleep_time)
        except Exception:
            print traceback.print_exc()
            
    
            
    #获取元素的文本值
    def getElementText(self,locators):
        logger=self.logger
        t1=time.time()
        try:
            text=[element[0].text for element in self.getElementAndInfos(locators)]
            if len(text) is 1:
                return text[0]
                logger.info("getElementText {0}  Spend {1} seconds".format(text[0],time.time()-t1))
            else:
                return text
                logger.info("getElementText {0}  Spend {1} seconds".format(text[-1],time.time()-t1))
        except TypeError:
            print traceback.print_exc()
     
