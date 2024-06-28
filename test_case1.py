# Test case 1: Positive LogIn test
# Open page
# Type username student into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Verify button Log out is displayed on the new page


# Test case 2: Negative username test
# Open page
# Type username incorrectUser into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your username is invalid!


# Test case 3: Negative password test
# Open page
# Type username student into Username field
# Type password incorrectPassword into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your password is invalid!


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://practicetestautomation.com/practice-test-login/")


user_input = browser.find_element(By.ID, "username")
user_input.send_keys("student")
password_input = browser.find_element(By.ID, "password")
password_input.send_keys("Password123")
submit_btn = browser.find_element(By.ID, "submit")
submit_btn.click()


verify_link = browser.find_element(
    By.CLASS_NAME, "post-title")

label = verify_link.get_attribute("innerHTML")

assert "Successfully" in label


log_out = browser.find_element(
    By.CLASS_NAME, "wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color"
)

log_out.click()
browser.quit()
print("Successful test!")
