#!/usr/bin/env python
#coding=utf-8
'''
Description:批量执行测试用例，并输出测试报告的模块

'''

import sys,os
import unittest,time
import HTMLTestRunner


src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

def createSuite():
    testunit=unittest.TestSuite()
    testcasePath=r"..\ScriptExcute"
    discover=unittest.defaultTestLoader.discover(testcasePath, pattern="Test*.py", top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            
    return testunit


def runSuite(suite):
    report_path = os.path.abspath('..\\TestReport\%s'%(time.strftime("%Y-%m-%d",time.localtime())))
    print report_path
    print "----------------------------------"
    if os.path.exists(report_path) is not True:
        os.mkdir(report_path)
    reportName_path = report_path+u"\美团App_AutoTestReport-%s.html"%(time.strftime(u"%H-%M",time.localtime()))
    fp=open(reportName_path,'wb')
#     for case in suite:
    runner = HTMLTestRunner.HTMLTestRunner(
                 stream=fp,
                 title='美团App自动化测试结果',
                 description='美团App自动化测试用例执行结果'
                 )
    
    runner.run(suite)   
    fp.close()


if __name__ == "__main__":
    #执行测试
    runSuite(createSuite())
