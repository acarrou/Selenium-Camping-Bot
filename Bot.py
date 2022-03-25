# create selenium bot that make a reservation on a website


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




# create a new instance of chrome
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# go to the website
driver.get(campground_link)
# wait for the page to load
button = driver.find_element(by=By.CLASS_NAME, value="sarsa-button.sarsa-modal-close-button.sarsa-button-subtle.sarsa-button-md")
button.click()
# find the first link on the page
link = driver.find_element(by=By.CLASS_NAME, value="sarsa-button.sarsa-button-primary.sarsa-button-md")
# click the link
link.click()

"rec-availability-date"

#IN PROGRESS
# wait for the page to load
first_day = number_of_days
while number_of_days>0 and int(camp_day)<=31:
    wait = WebDriverWait(driver, 10)
    button = driver.find_element(by=By.XPATH, value=f"//button[@aria-label='{camp_month} {camp_day}, 2022 - Site {camp_site_num} is available']")
    driver.execute_script("arguments[0].click();", button)

    camp_day = int(camp_day)
    if number_of_days == first_day:
        camp_day+=2
        number_of_days -=2
    camp_day+=1
    number_of_days-=1
    camp_day = str(camp_day)

'''# find the form
form = driver.find_element_by_id("reserve-form")
# find the first name field
first_name = form.find_element_by_name("firstname")
# enter first name
first_name.send_keys(first_name)
# find the last name field
last_name = form.find_element_by_name("lastname")
# enter last name
last_name.send_keys(last_name)
# find the credit card number field
cc_number = form.find_element_by_name("creditcardnumber")
# enter credit card number
cc_number.send_keys(credit_card)
# find the credit card expiration month field
cc_exp_month = form.find_element_by_name("cc_exp_month")
# enter credit card expiration month
cc_exp_month.send_keys(cc_exp_month)
# find the credit card expiration year field
cc_exp_year = form.find_element_by_name("cc_exp_year")
# enter credit card expiration year
cc_exp_year.send_keys(cc_exp_year)
# find the credit card cvv field
cc_cvv = form.find_element_by_name("cvv")
# enter credit card cvv
cc_cvv.send_keys(cvv)
# find the submit button
submit_button = form.find_element_by_name("submit")
# click submit
submit_button.click()'''

#<button class="rec-availability-date" aria-label="Mar 25, 2022 - Site APA09 is available">A</button>
#<button data-component="Button" type="button" class="sarsa-button availability-page-book-now-button-tracker availability-grid-book-now-button-tracker mobile sarsa-button-primary sarsa-button-md"><span class="sarsa-button-inner-wrapper"><span class="sarsa-button-content">Add to Cart</span></span></button>
