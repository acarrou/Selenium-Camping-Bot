# create selenium bot that make a reservation on a website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

campground_link = "https://www.recreation.gov/camping/campgrounds/273757"
#campground_link = "https://www.recreation.gov/camping/campgrounds/233116"
ChromeWebDriverPath = r"C:\chromedriver_win32\chromedriver.exe"

camp_month = "Mar"
camp_day = "25"
number_of_days = 5
camp_site_num = "APA09"

email_login = "adriencarrou@gmail.com"
password_login = "null"
credit_card = "1234567890123456"
cc_exp_month = "12"
cc_exp_year = "24"
cvv = "123"

# create a new instance of chrome
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# go to the website
driver.get(campground_link)
# wait for the page to load
button = driver.find_element(by=By.CLASS_NAME, value="sarsa-button.sarsa-modal-close-button.sarsa-button-subtle.sarsa-button-md")
button.click()
# find the first link on the page

#IN PROGRESS
# wait for the page to load
first_day = number_of_days
while number_of_days>0 and int(camp_day)<=31:
    button = driver.find_element(by=By.XPATH, value=f"//button[@aria-label='{camp_month} {camp_day}, 2022 - Site {camp_site_num} is available']")
    driver.execute_script("arguments[0].click();", button)

    camp_day = int(camp_day)
    if number_of_days == first_day:
        camp_day+=2
        number_of_days -=2
    camp_day+=1
    number_of_days-=1
    camp_day = str(camp_day)
driver.execute_script("window.scrollTo(0, 1000)")


'''
add_to_cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='sarsa-button.availability-page-book-now-button-tracker.availability-grid-book-now-button-tracker.mobile.sarsa-button-primary.sarsa-button-md']"))
)'''

driver.implicitly_wait(3)
add_to_cart = driver.find_element(by=By.XPATH, value="//*[@id='tabs-panel-0']/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/button[1]")
add_to_cart.click();

#Login to Account
'''email = driver.find_element(by=By.ID, value="email")
password = driver.find_element(by=By.ID, value="rec-acct-sign-in-password")
email.send_keys(email_login)
password.send_keys(password_login)
SignIn = driver.find_element(by=By.CLASS_NAME, value="sarsa-button rec-acct-sign-in-btn sarsa-button-primary sarsa-button-lg sarsa-button-fit-container")
SignIn.click()'''