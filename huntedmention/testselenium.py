'''
Created on 2019. 7. 2.

@author: Seleuchel
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.PhantomJS("D:\\Hyde\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("https://www.youtube.com/results?search_query=%EB%A9%94%EC%9D%B4%ED%94%8C%EC%8A%A4%ED%86%A0%EB%A6%AC")

print(driver.find_element_by_id("content").text)
driver.close()
