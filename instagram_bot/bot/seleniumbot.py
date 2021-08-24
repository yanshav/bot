from selenium import webdriver
import time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Bot:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.browser = webdriver.Chrome()
        self.list_name = []
        self.status = 777

    def check(self, name, password):
        self.browser.get('https://www.instagram.com/')
        time.sleep(1)
        input_login = self.browser.find_element(By.NAME, 'username')
        input_login.clear()
        input_login.send_keys(name)
        input_password = self.browser.find_element(By.NAME, 'password')
        input_password.clear()
        input_password.send_keys(password)
        self.browser.find_element_by_css_selector('button[type="submit"]').click()
        time.sleep(2)
        check = self.browser.find_elements_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        if check:
            return True
        else:
            return False

    def follow(self, hashtag, numb):
        try:
            self.browser.get('https://www.instagram.com/')
            time.sleep(random.randrange(3, 5))
            input_login = self.browser.find_element(By.NAME, 'username')
            input_login.clear()
            input_login.send_keys(self.login)
            time.sleep(random.randrange(1, 3))
            input_password = self.browser.find_element(By.NAME, 'password')
            input_password.clear()
            input_password.send_keys(self.password)
            time.sleep(1)
            self.browser.find_element_by_css_selector('button[type="submit"]').click()
            print('class', hashtag)
            time.sleep(10)
            self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
            time.sleep(3)

            numb_scroll = (int(numb) - 33) // 12
            if numb_scroll > 0:
                for i in range(int(numb_scroll + 1)):
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

            hrefs = self.browser.find_elements_by_tag_name('a')
            follow_list = []
            time.sleep(10)
            for elem in hrefs:
                href = elem.get_attribute('href')
                if '/p/' in href:
                    follow_list.append(href)

            counter = 0
            int_numb = int(numb)
            while counter < int_numb:
                # for i in follow_list:
                self.browser.get(follow_list[counter])
                # follow_click = self.browser.find_element(By.XPATH,
                # "/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button")
                name = self.browser.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a').text

                time.sleep(4)

                self.browser.get(f"https://www.instagram.com/{name}/")
                time.sleep(5)

                button_text = self.browser.find_element(By.XPATH,
                                                        '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')

                try:
                    button_text_of_if = self.browser.find_element(By.XPATH,
                                                                  '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')

                    print(button_text.text)

                    if button_text_of_if.text == 'Отправить сообщение':
                        counter += 1
                        int_numb += 1
                        time.sleep(5)
                        continue
                    else:
                        time.sleep(3)
                        button_text.click()
                        time.sleep(random.randrange(1, 5))
                        # like.click()
                        time.sleep(random.randrange(10))
                        counter += 1
                    if name not in self.list_name:
                        self.list_name.append(name)
                except:
                    button_text.click()
                    counter += 1
                    time.sleep(7)
                    if name not in self.list_name:
                        self.list_name.append(name)

                    continue

        except:
            self.status = 'error'

    def like(self, hashtag2, numb2):
        try:
            self.browser.get('https://www.instagram.com/')
            time.sleep(random.randrange(3, 5))
            input_login = self.browser.find_element(By.NAME, 'username')
            input_login.clear()
            input_login.send_keys(self.login)
            time.sleep(random.randrange(1, 3))
            input_password = self.browser.find_element(By.NAME, 'password')
            input_password.clear()
            input_password.send_keys(self.password)
            time.sleep(1)
            self.browser.find_element_by_css_selector('button[type="submit"]').click()
            time.sleep(10)

            self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag2}/")
            time.sleep(3)

            numb_scroll = (int(numb2) - 33) // 12
            if numb_scroll > 0:
                for i in range(int(numb_scroll + 1)):
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

            hrefs = self.browser.find_elements_by_tag_name('a')

            follow_list = []
            for elem in hrefs:
                href = elem.get_attribute('href')
                if '/p/' in href:
                    follow_list.append(href)

            counter = 0
            while counter < int(numb2):
                # for i in follow_list:
                self.browser.get(follow_list[counter])
                like_click = self.browser.find_element(By.XPATH,
                                                       "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                name = self.browser.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a').text

                button_like = self.browser.find_element(By.CSS_SELECTOR,
                                                        '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
                button_text = button_like.get_attribute('aria-label')

                if button_text == 'Не нравится':
                    counter += 1
                    time.sleep(5)
                    continue
                else:
                    time.sleep(4)
                    like_click.click()
                    time.sleep(random.randrange(1, 5))
                    # like.click()
                    time.sleep(random.randrange(10))
                    counter += 1
                if name not in self.list_name:
                    self.list_name.append(name)

        except:
            self.status = 'error'

    def comments(self, hashtag2, numb2, comments):
        try:
            comment_list = comments.split('/')

            self.browser.get('https://www.instagram.com/')
            time.sleep(random.randrange(3, 5))
            input_login = self.browser.find_element(By.NAME, 'username')
            input_login.clear()
            input_login.send_keys(self.login)
            time.sleep(random.randrange(1, 3))
            input_password = self.browser.find_element(By.NAME, 'password')
            input_password.clear()
            input_password.send_keys(self.password)
            time.sleep(1)
            self.browser.find_element_by_css_selector('button[type="submit"]').click()
            time.sleep(10)

            self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag2}/")
            time.sleep(3)

            numb_scroll = (int(numb2) - 33) // 12
            if numb_scroll > 0:
                for i in range(int(numb_scroll + 1)):
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

            hrefs = self.browser.find_elements_by_tag_name('a')

            follow_list = []
            for elem in hrefs:
                href = elem.get_attribute('href')
                if '/p/' in href:
                    follow_list.append(href)

            print('yes')

            counter = 0
            int_numb = int(numb2)
            while counter < int_numb:
                # for i in follow_list:
                self.browser.get(follow_list[counter])
                # follow_click = self.browser.find_element(By.XPATH,
                # "/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button")
                time.sleep(random.randint(4, 7))
                input_comment = self.browser.find_element(By.XPATH,
                                                          "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                input_comment.clear()
                input_comment.click()
                time.sleep(random.randint(1, 4))
                input_text = self.browser.find_element(By.XPATH,
                                                       "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                input_text.send_keys(random.choice(comment_list))
                time.sleep(random.randint(4, 7))
                button_comment = self.browser.find_element(By.XPATH,
                                                           "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]")
                button_comment.click()
                time.sleep(random.randint(3, 7))
                name = self.browser.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a').text
                if name not in self.list_name:
                    self.list_name.append(name)
                counter += 1
        except:
            self.status = 'error'

    def close_browser(self):
        self.browser.close()
        time.sleep(1)
        self.browser.quit()


if __name__ == '__main__':
    ac = Bot('olegpristavka_temp', 'instabot57')
    time.sleep(4)
    ac.comments('november', 2, 'like/cool/beautifull/beauty')
