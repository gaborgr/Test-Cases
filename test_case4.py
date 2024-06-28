from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.saucedemo.com/")


user_input = browser.find_element(By.ID, "user-name")
user_input.send_keys("standard_user")


password_input = browser.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_input = browser.find_element(By.ID, "login-button")
login_input.click()


add_prod1 = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_prod1.click()

add_prod2 = browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
add_prod2.click()

view_cart = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
view_cart.click()

checkout_btn = browser.find_element(By.ID, "checkout")
checkout_btn.click()

firstname_field = browser.find_element(By.ID, "first-name")
firstname_field.send_keys("Gabriel")

lastname_field = browser.find_element(By.ID, "last-name")
lastname_field.send_keys("Guerra")

postal_field = browser.find_element(By.ID, "postal-code")
postal_field.send_keys("7750000")

next_btn = browser.find_element(By.ID, "continue")
next_btn.click()

finish_btn = browser.find_element(By.ID, "finish")
finish_btn.click()

complete_txt = browser.find_element(By.CLASS_NAME, "title")

verification_text = complete_txt.get_attribute("innerHTML")

assert "Checkout: Complete!" in verification_text

browser.quit()

print("Successful test!")
