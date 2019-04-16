from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class InstagramBot:
    def __init__(self, username = 'here', password = 'here'): #enter your correct username and password
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.delay = 3 #wait for page loading

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(self.delay)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click() #login button
        
        time.sleep(self.delay)

    def like_photo(self, hashtag = 'here'): #hashtag goes here
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(self.delay)

        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(self.delay)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if 'p' in href.split('/')]


        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span').click()
                time.sleep(self.delay//2)
            except  Exception as e:
                print("\n\n"+e+'\n')
                time.sleep(2)

ig = InstagramBot()
ig.login()
ig.like_photo()
