import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# or '/usr/lib/chromium-browser/chromedriver' if you use chromium-chromedriver
driver.get('http://www.hackerrank.com/auth/login');
time.sleep(2) # Let the user actually see something!

# browser.find_element_by_xpath("//input[@type='email']”).send_keys("tsvxbard@sharklasers.com")
driver.find_element_by_xpath("//input[@type='text']").send_keys('tsxvbard@sharklasers.com')
driver.find_element_by_xpath("//input[@type='password']").send_keys('Password12345')

driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button/div/span").click()

time.sleep(2)
contest_submissions = "https://www.hackerrank.com/contests/snu-sprint-2/judge/submissions/1"

driver.get(contest_submissions)

# time.sleep(5) # Let the user actually see something!
# driver.quit() 
