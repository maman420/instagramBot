from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import random
import sys
import time


class instagramBot:
    username = 'yourUserName'
    password = 'yourPassword'

    likes = 0
    followed = 0
    comments_number = 0 

    hashtags = [
        'weightloss3weeks', #'weightlosssuccess', 'weightlossadvice', 'swweightloss', 'lowcarbweightloss',
        #'weightlossupport', 'fastweightloss', 'weightlosscoach', 'weightlossbeforeandafter', 'weightlossideas',
        #'weightlossstruggle', 'weightlossrecipes', 'weightlossblog', 'weightlosstip', 'weightlosschallenge',
        #'weightlossprogress', 'weightlosss', 'weightlossproblems', 'weightlossfoods', 'myweightloss', 
    ]
#        'weightlosssuccess', 'fitnesstransformation', 'weightlossfood', 'weightlossprogress',
#        'transformation', 'weightlosstransformation', 'weightlossgoals', 'fatlossjourney',
#        'weightlossjourney', 'weightlossmotivation', 'fatloss', 'weightlosstips','weightloss',
#        'health', 'fitness', 'fitnessmotivation', 'weightloss', 'weightlossjourney', 
#        'healthyfood', 'diet', 'dietfood', 'loseweightfast', 'loseweịght',
    
#        'hustle', 'cash', 'startup', 'bitcoin', 'forex', 'entrepreneurship', 'money', 'finance', 'boss', 'stocks', 'invest',
#        'successful', 'investing', 'work', 'passion', 'billionaire', 'grind', 'trading',
#        'financialprofessional', 'marketing', 'digitalmarketing', 'marketingdigital', 'onlinemarketing',

    comments = [
        'Your posts are amazing', 'Amazing work. Keep going!', 'Your photos are magnificent',
        'Your work fascinates me!', 'I like how you put your posts together', 'Great job',
        'What a really nice photo, great job!', 'Well done!', 'Your posts are amazing',
    ]

    links = []
   

    def __init__(self):
        #chromedriver = "C:\\Users\TM160\Downloads\chromedriver_win32\geckodriver.log"
        self.browser = webdriver.Chrome()
        self.login()
        self.hustle()

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(4)

        username_field = self.browser.find_element(By.NAME, 'username')
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(1)

        password_field = self.browser.find_element(By.NAME, 'password')
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(6)

    def hustle(self):
        self.getTopPosts()
        self.execute()
        self.finalize()

    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
            time.sleep(4)

            links = self.browser.find_elements(By.TAG_NAME, 'a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            try:
                for i in range(0, 10, 1):
                    link = valid_links[i].get_attribute('href')
                    if link not in self.links:
                        self.links.append(link)
            except:
                print("an error occured")

    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(4)
            
            #click on follow only when Follow text apear(instead of doing followed list)
            if self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button').text == 'Follow':        
                self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()       
                self.followed += 1
                time.sleep(1)

                self.comment()
                self.like()

                sleeptime = random.randint(2,4)
                time.sleep(sleeptime)

    def comment(self):
        _comment = random.choice(self.comments)

        comment_input = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/textarea')
        comment_input.click()
        comment_input = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/textarea')
        comment_input.send_keys(_comment)
        time.sleep(1)
        comment_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        self.comments_number += 1
            
    def like(self):
        like_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
        like_button.click()
        self.likes += 1
        time.sleep(2)

    def finalize(self):
        print('Liked ' + str(self.likes) + ' photos.')
        print('Commented ' + str(self.comments_number) + ' photos.')
        print('Followed ' + str(self.followed)+ ' new people.')

        self.browser.close()
        sys.exit()

instagramBot = instagramBot()

