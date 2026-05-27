"""
Автотест для https://demoqa.com/buttons
С корректными assert сообщениями для каждого шага
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
    """Тест проверяет двойной и правый клик на кнопках"""
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    try:
        # Шаг 1: Открытие страницы
        driver.get("https://demoqa.com/buttons")
        
        # Шаг 2: Поиск и проверка наличия кнопки двойного клика
        double_click_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "doubleClickBtn"))
        )
        assert double_click_btn is not None, "Кнопка 'Double Click Me' не найдена на странице"
        assert double_click_btn.is_displayed(), "Кнопка 'Double Click Me' не отображается на странице"
        print("✓ Кнопка двойного клика найдена и отображается")
        
        # Шаг 3: Выполнение двойного клика
        ActionChains(driver).double_click(double_click_btn).perform()
        print("✓ Выполнен двойной клик по кнопке")
        
        # Шаг 4: Проверка появления сообщения после двойного клика
        double_click_msg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "doubleClickMessage"))
        )
        assert double_click_msg.is_displayed(), "Сообщение о двойном клике не появилось после выполнения double_click"
        assert double_click_msg.text == "You have done a double click", \
            f"Ожидался текст 'You have done a double click', получен '{double_click_msg.text}'"
        print("✓ Сообщение о двойном клике успешно отображается")
        
        # Шаг 5: Поиск и проверка наличия кнопки правого клика
        right_click_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "rightClickBtn"))
        )
        assert right_click_btn is not None, "Кнопка 'Right Click Me' не найдена на странице"
        assert right_click_btn.is_displayed(), "Кнопка 'Right Click Me' не отображается на странице"
        print("✓ Кнопка правого клика найдена и отображается")
        
        # Шаг 6: Выполнение правого клика
        ActionChains(driver).context_click(right_click_btn).perform()
        print("✓ Выполнен правый клик по кнопке")
        
        # Шаг 7: Проверка появления сообщения после правого клика
        right_click_msg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "rightClickMessage"))
        )
        assert right_click_msg.is_displayed(), "Сообщение о правом клике не появилось после выполнения context_click"
        assert right_click_msg.text == "You have done a right click", \
            f"Ожидался текст 'You have done a right click', получен '{right_click_msg.text}'"
        print("✓ Сообщение о правом клике успешно отображается")
        
        print("\n✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        
    except AssertionError as e:
        print(f"\n❌ ОШИБКА ПРОВЕРКИ: {e}")
        raise  # Пробрасываем исключение дальше, чтобы тест упал с понятным сообщением
        
    except Exception as e:
        print(f"\n❌ НЕПРЕДВИДЕННАЯ ОШИБКА: {e}")
        raise
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_buttons_demoqa()
