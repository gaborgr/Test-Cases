# Test case 3: Negative password test
# 1. Open page
# 2. Type username student into Username field
# 3. Type password incorrectPassword into Password field
# 4. Push Submit button
# 5. Verify error message is displayed
# 6. Verify error message text is Your password is invalid!

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://practicetestautomation.com/practice-test-login/")


user_input = browser.find_element(By.ID, "username")
user_input.send_keys("student")
password_input = browser.find_element(By.ID, "password")
password_input.send_keys("Password124")
submit_btn = browser.find_element(By.ID, "submit")
submit_btn.click()


verify_error = browser.find_element(
    By.ID, "error")


invalid_user = verify_error.get_attribute("innerHTML")

assert "Your password is invalid!" in invalid_user
browser.quit()

print("Successful test!")
