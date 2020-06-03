from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import gen
import get_code_gmail
import os

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

#checks if device blocked by verify device
time.sleep(2)
while(web.current_url=='https://github.com/sessions/verified-device'):

    time.sleep(3)

    try:
        code = get_code_gmail.main()
        web.find_element_by_id('otp').send_keys(code)
        web.find_element_by_xpath('/html/body/div[3]/main/div/div[3]/form/button').click()

    except:

        web.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/button').click()

with open("reponame") as f:
    sub = f.read()

link = "https://www.github.com/"+username+"/"+sub+"/upload/master"
web.get(link)

time.sleep(2)
newfile = gen.gen_file()
web.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div[2]/form[2]/file-attachment/p/input').send_keys(os.getcwd()+"/"+newfile)

time.sleep(10)
web.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/form/button').click()
