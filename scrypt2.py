import time
import traceback
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchDriverException

def check_phone_on_sites(phone_number):
    sites = [
        "https://www.google.com",
        "https://www.sberbank.ru",
        "https://vk.ru",
        "https://ok.ru",
        "https://beruberi.ru",
        "https://krediska.ru",
        "https://oneclickmoney.ru"
    ]

    # Путь к geckodriver
    gecko_driver_path = r"C:\Users\donvo\Desktop\geckodriver.exe"  # Убедитесь, что путь к geckodriver правильный

    # Настройка опций Firefox
    firefox_options = Options()
    firefox_options.add_argument("--headless")

    # Сервис для Firefox
    service = Service(gecko_driver_path)

    for site in sites:
        try:
            driver = webdriver.Firefox(service=service, options=firefox_options)
            driver.get(site)
            time.sleep(2)  # Ждем, пока страница загрузится

            # Здесь добавьте код для поиска номера телефона на каждой странице
            # Например, используйте driver.find_element(By.XPATH, ...) или другой подходящий метод

            driver.quit()
        except NoSuchDriverException as e:
            print(f"Ошибка проверки номера телефона {phone_number} на сайте {site}: {e.msg}")
        except Exception as e:
            print(f"Ошибка проверки номера телефона {phone_number} на сайте {site}: {e}")
            print(traceback.format_exc())

# Пример вызова функции
check_phone_on_sites("89043505444")
check_phone_on_sites("89057190493")
