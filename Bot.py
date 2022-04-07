# create selenium bot that make a reservation on a website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

campground_link = "https://www.recreation.gov/camping/campgrounds/232755"
#campground_link = "https://www.recreation.gov/camping/campgrounds/233116"
ChromeWebDriverPath = r"C:\chromedriver_win32\chromedriver.exe"

camp_month = "Jun"
camp_day = "5"
number_of_days = 5
group_amount = 4
camp_site_num = "006"
    #"APA09"
#001-033 for Big Sur campground

email_login = "adriencarrou@gmail.com"
password_login = "ForTesting12345"
postal_code = "94025"
first_name = "Adrien"
last_name = "Carrou"
credit_card_num = "1234567890123456"
cc_exp_month = "12"
cc_exp_year = "24"
cvv = "123"

# create a new instance of chrome for linux
#driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(executable_path=ChromeWebDriverPath) #For Windows

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
driver.implicitly_wait(3)
email = driver.find_element(by=By.ID, value="email")
password = driver.find_element(by=By.ID, value="rec-acct-sign-in-password")
email.send_keys(email_login)
password.send_keys(password_login)
SignIn = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/form/button")
SignIn.click()

#------This should be uncommented if the campground does not have accessibility flag
'''driver.implicitly_wait(3)
AccessButton = driver.find_element(by=By.XPATH, value="//*[@id='accessibility-modal-alert']/div/div/div/div/div/div/div/button[2]")
AccessButton.click()'''

driver.implicitly_wait(5)
postal = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[2]/section[1]/div[2]/div[2]/div[3]/div[3]/div/div[2]/div[1]/input")
postal.send_keys(postal_code)


driver.implicitly_wait(3)
group_size = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[2]/section[1]/div[2]/div[3]/div/div/div/div/div[2]/button[2]")
while group_amount > 0:
    group_size.click()
    group_amount-=1

driver.implicitly_wait(3)
car_amount = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[2]/section[1]/div[2]/div[5]/div/div/div/div/div[2]/button[2]")
car_amount.click() #add another click() if you want to add more than one car. This might cause an error if the campsite doesn't allow more than one car.

driver.implicitly_wait(3)
accept_terms = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[2]/section[2]/div[3]/label/span")
accept_terms.click()

updater = Updater("5273245540:AAEUT573S0buicRc2876h5O9_uF30JDmQko",
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "I am the camping bot here to help you when there is an available spot for you in your specified camp ground. I will notify you when your spot is available!")

    update.message.reply_text(
        f"Hello {first_name}! There is an available spot camping spot for you, and you have 15 minutes to fully reserve your spot!!! {driver.current_url}")
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()

#/html/body/div[14]/div/div/div/div[2]/button[1]

'''driver.implicitly_wait(10)
boat_equipment = driver.find_element(by=By.CLASS_NAME, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[2]/section[1]/div[3]/div[4]/div/div[1]/div/div/label/span[1]")
boat_equipment.click()

driver.implicitly_wait(5)
boat_length = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[2]/section[1]/div[3]/div[4]/div/div/div/div/div/div[2]/div[1]/input")
boat_length.send_keys(10)'''

'''driver.implicitly_wait(5)
go_to_cart = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/section/div/div[1]/div[3]/div/div/div/div[2]/button")
go_to_cart.click()

driver.implicitly_wait(5)
go_to_payment = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div/div/div[3]/button")
go_to_payment.click()


driver.implicitly_wait(5)
payment_first_name = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/input")
payment_first_name.send_keys(credit_first_name)

driver.implicitly_wait(5)
payment_last_name = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/input")
payment_last_name.send_keys(credit_last_name)

driver.implicitly_wait(5)
cc_num = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/input")
cc_num.send_keys(credit_card_num)

driver.implicitly_wait(5)
exp_month = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[1]/select")
exp_month.is_selected(cc_exp_month)

driver.implicitly_wait(5)
exp_year = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/select")
exp_year.is_selected(cc_exp_year)


driver.implicitly_wait(5)
security_cvv = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[4]/div/input")
security_cvv.send_keys(credit_card_num)

driver.implicitly_wait(5)
next_pay = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button")
next_pay.send_keys(credit_card_num)'''




