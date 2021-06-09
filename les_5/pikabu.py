from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains # для скрола тут, и например комб клавиш
from time import sleep

chrome_options = Options() # создаем обьект
chrome_options.add_argument('start-maximized') # 'start-maximized' - развернутый экран

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://pikabu.ru/')

for i in range(5):
    article = driver.find_elements_by_tag_name('article')
    action = ActionChains(driver)

    # action.key_down(Keys.LEFT_CONTROL).key_down(Keys.C).key_up(Keys.LEFT_CONTROL).key_up(Keys.C) # зажатие клавиш и оптустить
    action.move_to_element(article[-1])

    action.perform() # запуск
    sleep(4)





