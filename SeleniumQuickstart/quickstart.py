from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Connecting to the website
driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver.exe')
driver.get("https://inspirobot.me")

# Waiting for the page to load
button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-generate"))
    )
# Clicking the generate button
button.click()

# Waiting for the image to load
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "generated-image"))
    )

# Saving the image
open('output.png','wb').write(element.screenshot_as_png)

# Closing the browser
driver.close()

# Creating the driver in headless mode
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'./webdriver/geckodriver.exe')
