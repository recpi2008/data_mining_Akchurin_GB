from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait # для задержек
from selenium.webdriver.support import expected_conditions as EC # условия задержки
from selenium.webdriver.common.by import By

# from time import sleep

chrome_options = Options() # создаем обьект
chrome_options.add_argument('start-maximized') # 'start-maximized' - развернутый экран

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://dixy.ru/catalog/')

# driver.refresh() # обновляет страницу

pages = 0
while pages<3:
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'view-more')) # presence_of_element_located - пока элемент не появится,
        )                              # element_to_be_clickable - пока элемент не станет кликабельным
        # button = driver.find_element_by_class_name('view-more')
        # # print(1)
        button.click()
        pages +=1
    except:
        print(pages)
        break
goods = driver.find_elements_by_class_name('dixyCatalogItem')
# print(1)
for good in goods:
    print(good.find_element_by_class_name('dixyCatalogItem__title').text)
    print(good.find_element_by_class_name('dixyCatalogItemPrice__new').text)


