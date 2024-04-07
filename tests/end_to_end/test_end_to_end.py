from selenium import webdriver
from selenium.webdriver.common.by import By

def test_bmi_calculation():
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:5000")

        height_input = driver.find_element(By.ID, 'height')
        weight_input = driver.find_element(By.ID, "weight")
        submit_button = driver.find_element(By.ID, "submit_bmi_form")

        height_input.send_keys("69")
        weight_input.send_keys("160")

        submit_button.click()

        result_element = driver.find_element(By.ID, "result")
        assert "Your BMI is: 24.2" in result_element.text
        assert "You are classified as Normal Weight" in result_element.text

    finally:
        driver.quit()