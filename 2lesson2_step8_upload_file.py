from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("Den")

    surname = browser.find_element_by_name("lastname")
    surname.send_keys("Fursov")

    mail = browser.find_element_by_name("email")
    mail.send_keys("test@gmail.com")

    uploadFile = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    uploadFile.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
