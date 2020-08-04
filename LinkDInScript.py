from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from time import sleep


#change path to your local chromedriver.exe

linkcon = webdriver.Chrome("C:\linkdinscript-master\chromedriver.exe")
linkcon.maximize_window()

username = input("Enter Your Email ")
password = input("Enter Your Password ")


linkcon.get("https://www.linkedin.com/")
linkcon.find_element_by_xpath("//input[@name='session_key']").send_keys(username)
linkcon.find_element_by_xpath("//input[@name='session_password']").send_keys(password)
sleep(2)
linkcon.find_element_by_xpath("//button[contains(.,'Sign in')]").click()
linkcon.find_element_by_id("mynetwork-nav-item").click()

sleep(4)
body = linkcon.find_element_by_tag_name("body")
for _ in range(10):
    body.send_keys(Keys.END)
    sleep(2)
    body.send_keys(Keys.HOME)

cont = linkcon.find_elements_by_xpath("//button[contains(.,'Connect')]")

for x in cont:
    print('{}/{}'.format(x, len(cont)))
    sleep(2)
    x.click()

