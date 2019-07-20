from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class bot:

    def __init__(self,email,password):
        self.driver = webdriver.Chrome("D:\Sourav (softwares)\chromedriver.exe")
        self.email=email
        self.password=password
    def login(self):
        driver=self.driver
        driver.get("https://www.instagram.com/")
        driver.find_element_by_xpath("//button[contains(text(),'Log in with Facebook')]").click()
        email=driver.find_element_by_xpath("//input[@name='email']")
        email.send_keys(self.email)
        password=driver.find_element_by_xpath("//input[@name='pass']")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(6)
        notnow=driver.find_element_by_xpath("//button[contains(@class,'HoLwm')]")
        notnow.click()
    def like(self,hashtag):
        driver=self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range(1,6):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs=driver.find_elements_by_tag_name("a")
        pics=[elems.get_attribute("href") for elems in hrefs]
        pics=[href for href in pics]
        print(hashtag+"="+str(len(pics)))
        count=0
        for links in pics:
            driver.get(links)
            try:
                driver.find_element_by_xpath("//button[contains(@class,'dCJp8 afkep _0mzm-')]//span[contains(@class,'glyphsSpriteHeart__outline__24__grey_9 u-__7')]").click()
                count=count+1
                print("Liking Pic No="+str(count))
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(18)
            except Exception as e:
                time.sleep(2)












































sourav= bot("sarkersourav55@gmail.com","@sarker.sourav.55")
sourav.login()
sourav.like("Bangladeshi")





















































