from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


def check_phone_number(phone_number, url):
    options = Options()
    options.headless = True  # Запуск браузера в фоновом режиме

    # Использование webdriver_manager для автоматической установки драйвера
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(url)

    # Выполнение логики проверки номера телефона на странице
    # Пример:
    # phone_input = driver.find_element(By.NAME, 'phone')
    # phone_input.send_keys(phone_number)
    # submit_button = driver.find_element(By.ID, 'submit')
    # submit_button.click()

    # Имитация проверки номера телефона
    print(f"Проверка номера {phone_number} на сайте {url}")

    driver.quit()


# Примеры использования функции
phone_numbers = ['89043505444', '89057190493']
urls = ['https://google.com', 'https://sberbank.ru', 'https://vk.ru', 'https://ok.ru', 'https://beruberi.ru',
        'https://krediska.ru', 'https://oneclickmoney.ru']

for phone_number in phone_numbers:
    for url in urls:
        check_phone_number(phone_number, url)
