from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_return(driver, element_id, el_type = By.ID):
    """
    Wait for the element to be present and return it.
    """
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((el_type, element_id))
    )

# Connecting to the website
driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver.exe')
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Waiting for the page to load
button = wait_and_return(driver, "accept-choices")
# Clicking the generate button
button.click()

# Retrieving the form First Name
form_fname = wait_and_return(driver, "fname")
# Retrieving the form Last Name
form_lname = wait_and_return(driver, "lname")

# Sending input
form_fname.clear()
form_fname.send_keys("Hello")
form_lname.clear()
form_lname.send_keys("World")

# Submitting the form
submit_button = wait_and_return(driver, "input[type=submit]", By.CSS_SELECTOR)
submit_button.click()

# Changing Window
windows = driver.window_handles
driver.switch_to.window(windows[1])

# Printing the result
return_value = wait_and_return(driver, "w3-container", By.CLASS_NAME)
print(return_value.text)
