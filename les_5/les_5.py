# сайт GB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://gb.ru/login')

login = driver.find_element_by_id('user_email')
login.send_keys('ivaneleskin2019@gmail.com')

password = driver.find_element_by_id('user_password')
password.send_keys('Ii786311')

login.send_keys(Keys.ENTER)

profile = driver.find_element_by_class_name('avatar')
driver.get(profile.get_attribute('href'))

profile_button = driver.find_element_by_class_name('text-sm')
driver.get(profile_button.get_attribute('href'))

# выборка элементов из выпадающего списка (поле множественного выбора)
gender = driver.find_element_by_name('user[gender]')
options = gender.find_elements_by_tag_name('option')
for option in options:
    if option.text == 'Мужской':
        option.click()

gender.submit() # сохраняем форму
driver.quit()


# print(1)