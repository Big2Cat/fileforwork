#!/usr/bin/env python
# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def main():

    driver = webdriver.Chrome()

    driver.get('http://localhost:8000/')

    WebDriverWait(driver, 30).until(lambda the_driver: the_driver.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']").is_displayed())
    WebDriverWait(driver, 30).until(lambda the_driver: the_driver.find_element_by_xpath("//div[@class='gt_cut_bg gt_show']").is_displayed())
    WebDriverWait(driver, 30).until(lambda the_driver: the_driver.find_element_by_xpath("//div[@class='gt_cut_fullbg gt_show']").is_displayed())


    element = driver.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")

    print '第一步，点击元素'
    ActionChains(driver).click_and_hold(on_element = element).perform()
    time.sleep(1)

    print "第二步，拖动元素"
    ActionChains(driver).move_to_element_with_offset(to_element = element, xoffset = 200,yoffset=50).perform()
    time.sleep(1)

    print '第三步，释放鼠标'
    ActionChains(driver).release(on_element = element).perform()

    time.sleep(3)

if __name__ == '__main__':

    main()
