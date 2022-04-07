
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