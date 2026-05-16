from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser
driver = webdriver.Chrome()

# Open Safora Contact Page
driver.get("https://safora.se/en/contact.html")

# Maximize window
driver.maximize_window()

time.sleep(2)

# Fill Name
name = driver.find_element(By.NAME, "name")
name.send_keys("Steffani Silva")

# Fill Email
email = driver.find_element(By.NAME, "email")
email.send_keys("silvasteffani2004@gmail.com")

# Fill Phone
phone = driver.find_element(By.NAME, "phone")
phone.send_keys("0740148998")

# Fill Message
message = driver.find_element(By.NAME, "message")
message.send_keys(
    "Hello Safora Team, this is a QA automation test submission."
)

time.sleep(2)

# Click Submit Button
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()

time.sleep(5)

print("Test executed successfully.")

# Close browser
driver.quit()