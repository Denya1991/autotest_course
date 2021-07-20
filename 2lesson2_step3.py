from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def summa(a, b):
        return a + b

    firstNum = browser.find_element_by_id("num1")
    first = int(firstNum.text)
    secondNum = browser.find_element_by_id("num2")
    second = int(secondNum.text)
    equal = str(summa(first, second))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(equal)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()