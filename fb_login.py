from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from time import sleep 


# create webdriver and dismiss alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')

# access url
#url = input()
driver.get('https://www.facebook.com/fixbugtinhyeu/posts/217368260408850')
sleep(3)

# login facebook
driver.find_element_by_id('email').send_keys('dphamhuukhanh@gmail.com')
driver.find_element_by_id('pass').send_keys('phamhuukhanhduy09122001')
driver.find_element_by_id('pass').send_keys(Keys.ENTER)
sleep(5)


links = driver.find_element_by_tag_name('span')
print(links)

#driver.close()

