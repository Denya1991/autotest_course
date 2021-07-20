from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    name = browser.find_element_by_tag_name("button")
    name.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value")
    x = int(x.text)
    y = y = calc(x)

    input_area = browser.find_element_by_class_name("form-control")
    input_area.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
