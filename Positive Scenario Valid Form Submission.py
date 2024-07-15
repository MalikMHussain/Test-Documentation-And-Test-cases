#•	Positive Scenario: Valid Form Submission
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

def test_valid_form_submission(): 
    driver = webdriver.Chrome()
    driver.get("https://example.com/register")    

    # Fill in the form
    driver.find_element(By.ID, "full_Name").send_keys("Hussain")
    driver.find_element(By.ID, "email").send_keys("hussain@yopmail.com")
    driver.find_element(By.ID, "password").send_keys("Hussain@123")
    driver.find_element(By.ID, "confirm_Password").send_keys("Hussain@123")
    driver.find_element(By.ID, "dob").send_keys("1990-01-01")
    driver.find_element(By.ID, "gender").send_keys("Male")
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "submit").click()    

    # Wait for the welcome page to load and check for the welcome message

    WebDriverWait(driver, 10).until(EC.url_contains("/welcome"))
    assert "Welcome, Hussain" in driver.page_source    

    driver.quit()

if name == "main":
    test_valid_form_submission()
