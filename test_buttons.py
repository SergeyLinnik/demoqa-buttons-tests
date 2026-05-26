"""
Автотест для https://demoqa.com/buttons
С автоматической загрузкой ChromeDriver через webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_buttons_demoqa():
    # Автоматическая установка и настройка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://demoqa.com/buttons")
    
    try:
        # Ожидание и поиск кнопок
        double_click_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "doubleClickBtn"))
        )
        right_click_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "rightClickBtn"))
        )
        
        # Двойной клик
        ActionChains(driver).double_click(double_click_btn).perform()
        print("✓ Выполнен двойной клик")
        
        # Проверка сообщения
        double_click_msg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "doubleClickMessage"))
        )
        assert double_click_msg.is_displayed()
        print("✓ Сообщение о двойном клике появилось")
        
        # Правый клик
        ActionChains(driver).context_click(right_click_btn).perform()
        print("✓ Выполнен правый клик")
        
        # Проверка сообщения
        right_click_msg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "rightClickMessage"))
        )
        assert right_click_msg.is_displayed()
        print("✓ Сообщение о правом клике появилось")
        
        print("\n✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_buttons_demoqa()