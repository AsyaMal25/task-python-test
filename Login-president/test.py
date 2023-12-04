from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def positive_login_test():
    driver = webdriver.Chrome()
    driver.get("https://xn--80afcdbalict6afooklqi5o.xn--p1ai/identity/account/login")

    email_input = driver.find_element(By.ID, "Username")
    password_input = driver.find_element(By.ID, "Password")
    login_button = driver.find_element(By.ID, "loginBtn")

    email_input.send_keys("testmail222555@gmail.com")
    password_input.send_keys("mM3k3.LSFmDdF4B")
    login_button.click()

    time.sleep(2) #Обработка запроса

    # Ожидание нужного URL
    expected_url = "https://xn--80afcdbalict6afooklqi5o.xn--p1ai/user/profile"
    time.sleep(5)

    # Проверяем, что текущий URL соответствует ожидаемому
    assert driver.current_url == expected_url

    driver.quit()

def negative_login_test():
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен драйвер для браузера (например, ChromeDriver)
    driver.get("https://xn--80afcdbalict6afooklqi5o.xn--p1ai/identity/account/login")

    email_input = driver.find_element(By.ID, "Username")
    wrong_password_input = driver.find_element(By.ID, "Password")
    login_button = driver.find_element(By.ID, "loginBtn")

    email_input.send_keys("testmail222555@gmail.com")
    wrong_password_input.send_keys("mM3k3.LSFmDdF4B111")
    login_button.click()

    time.sleep(2)  # Обработка запроса

    error_message_element = driver.find_element(By.CSS_SELECTOR, 'span[data-valmsg-for="Password"].text-danger.field-validation-error')
    error_message = error_message_element.text

    assert "Неверный логин или пароль" in error_message #Проверяю, что появилось сообщение об ошибке


    driver.quit()

# Запуск тестов
positive_login_test()
negative_login_test()

