# create selenium bot that make a reservation on a website


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

first_name = "Adrien"
last_name = "Carrou"
credit_card = "1234567890123456"
cc_exp_month = "12"
cc_exp_year = "24"
cvv = "123"



# create a new instance of chrome
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
# go to the website
driver.get("https://www.recreation.gov/camping/campgrounds/233116")
# wait for the page to load
button = driver.find_element_by_class_name("sarsa-button.sarsa-modal-close-button.sarsa-button-subtle.sarsa-button-md")
button.click()
# find the first link on the page
link = driver.find_element_by_class_name("sarsa-button.sarsa-button-primary.sarsa-button-md")
# click the link
link.click()



#IN PROGRESS
# wait for the page to load
WebDriverWait(driver, 10).until(
    lambda driver: driver.find_element_by_id("reserve-form")
)
# find the form
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
submit_button.click()
