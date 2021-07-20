from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    price = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    element = browser.find_element_by_id("input_value")
    x = int(element.text)
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    print(addToClipBoard)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()