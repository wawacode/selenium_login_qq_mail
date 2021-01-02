#coding=utf8
from selenium import webdriver
import time
'''
    打开浏览器
'''
def open_browser():
    browser=webdriver.Firefox()
    return browser
'''
    打开测试url
'''
def open_url(browser,url):
    browser.get(url)
    browser.maximize_window()
'''
    查找元素
'''
def find_element(browser,link_text,usr_id,pwd_id,btn_id):
    if link_text:
        browser.find_element_by_link_text(link_text).click()
    usrElement=browser.find_element_by_id(usr_id)
    pwdElement=browser.find_element_by_id(pwd_id)
    btnElement=browser.find_element_by_id(btn_id)
    return usrElement,pwdElement,btnElement
'''
    对查找的元素赋值
'''
def set_vals(elem,usr_txt,pwd_txt):

    listkey=[usr_txt,pwd_txt]
    i=0
    for key in listkey:
        elem[i].clear()
        elem[i].send_keys(key)
        i+=1
    elem[i].click()
'''
获取对应测试结果
'''
def get_result(browser,class_name):
    elems=browser.find_elements_by_class_name(class_name)
    for el in elems:
        print (el.text)
    time.sleep(10)
'''
关闭登陆效果，并关闭浏览器
'''
def close(browser):
    browser.find_element_by_link_text("退出").click()
    browser.close()
    '''
    进入对应框架内
    '''
def open_frame(browser,framename=""):
    if framename!="":
        browser.switch_to.frame(framename)
'''
    返回根
'''
        
def return_frame(browser):
    browser.switch_to_default_content()

'''
    进入页面的操作
'''
def get_response(browser,action_txt):
    browser.find_element_by_partial_link_text(action_txt).click()


if __name__=="__main__":
    '''
                                此段代码被修改
        driver=webdriver.Firefox()
    '''
    driver=open_browser()
    '''
                                此段代码被修改
        driver.get("http://mail.qq.com")
    '''
    open_url(driver,"http://mail.qq.com")
    '''
                            此段代码被修改
        driver.switch_to.frame("login_frame")
    '''
    open_frame(driver,"login_frame")
    '''
                            此段代码被修改
        label=driver.find_element_by_link_text(u"帐号密码登录").click()
        usr=driver.find_element_by_id("u")
        pwd=driver.find_element_by_id("p")
        btn=driver.find_element_by_id("login_button")
    '''
    elem_tmp=find_element(driver,u"帐号密码登录","u","p","login_button")
    '''
                            此段代码被修改
        usr..send_keys("XXXXXXXX")
        pwd..send_keys("XXXXXXXXXXXXXX")
        btn.click()
    '''
    set_vals(elem_tmp,"qq_hao","mima")
    '''
                        此段代码换成公用的切换回主界面的代码
           driver.switch_to_default_content()
    '''
    return_frame(driver)
    '''
                    此段代码换成功能性代码
        driver.find_element_by_partial_link_text(u"收件箱").click()
    '''
    get_response(driver,u"收件箱")
    '''
           此段回到相关frame
   '''
    open_frame(driver,"mainFrame")
    '''
                此段获取功能结果    
    '''
    get_result(driver,"F")
    '''
        此段代码退出
    '''
    return_frame(driver)
    close(driver)
