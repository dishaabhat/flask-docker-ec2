from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace this URL with the URL of your Flask application
APP_URL = 'http://localhost:5000'

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

try:
    # Open the Flask application URL
    driver.get(APP_URL)

    # Wait for the "Hello, World!" text to be present on the page
    hello_world_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Hello, World!')]"))
    )

    # Print success message if the text is found
    print("Flask Application Test: PASSED")

except Exception as e:
    # Print error message if any exception occurs
    print("Flask Application Test: FAILED")
    print(e)

finally:
    # Close the browser window
    driver.quit()
