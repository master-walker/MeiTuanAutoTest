##!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月29日

'''

import unittest 
from ComLib import Public

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Public.get_logger()
        self.driver = Public.getDriver()
        self.logger.info("\n")
        self.logger.info('############################### START ###############################')

    
    def tearDown(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
        
        
    