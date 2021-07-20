from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
		
    chest = browser.find_element_by_id("treasure")
    x = chest.get_attribute("valuex")
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()