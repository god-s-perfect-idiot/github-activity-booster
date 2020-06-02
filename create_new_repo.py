from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import gen

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
#options.add_argument('headless') #uncomment if u want no gui feedback.
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

web = webdriver.Chrome(options=options)
wait = WebDriverWait(web,10)


web.get('https://www.github.com/login')

username = ''    #username here
password = ''    #password here

reponame = gen.gen()+'-active-boosted'
reporm = "Boosted repo added to fill git activity grid. For details, check out github-activity-booster."

time.sleep(2)

user = web.find_element_by_id('login_field')
user.send_keys(username)
pw = web.find_element_by_id('password')
pw.send_keys(password)

time.sleep(1)
web.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]').click()

time.sleep(2)
web.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a').click()

time.sleep(2)
web.find_element_by_id('repository_name').send_keys(reponame)
web.find_element_by_id('repository_auto_init').click()
web.find_element_by_id('repository_description').send_keys(reporm)
web.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/button').click()

with open('reponame','w') as f:
    f.write(reponame)
