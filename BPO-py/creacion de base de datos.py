# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get("https://qa.dyalogo.cloud/manager/login.php")
driver.set_window_size(1382, 736)
driver.find_element(By.NAME, "txtUsuario").send_keys("santicri163@gmail.com")
    # 4 | type | name=txtPassword | MqwoOP19
driver.find_element(By.NAME, "txtPassword").send_keys("MqwoOP190")
    # 5 | click | name=txtUsuario | 
driver.find_element(By.NAME, "txtUsuario").click()
driver.find_element(By.CSS_SELECTOR, ".col-xs-4 > .btn").click()
    # 6 | type | name=txtUsuario | senadyalogo@gmail.coms
driver.find_element(By.NAME, "txtUsuario").send_keys("santicri163@gmail.com")
    # 7 | type | name=txtPassword | 123456789
driver.find_element(By.NAME, "txtPassword").send_keys("JaaeGyfF")
    # 8 | click | css=.col-xs-4 > .btn | 
driver.find_element(By.CSS_SELECTOR, ".col-xs-4 > .btn").click()


    # 9 | click | css=.select2-container--below .select2-selection__arrow | 
time.sleep(3)
 # Test name: Creacion de base de datos
 # Step # | name | target | value
 # 1 | open | https://qa.dyalogo.cloud/manager/modulo/guion/02f0858f054629ab02fea45f8d262b83 | 
driver.get("https://qa.dyalogo.cloud/manager/modulo/guion/02f0858f054629ab02fea45f8d262b83")
# 2 | setWindowSize | 1552x839 | 
driver.set_window_size(1552, 839)
# 3 | click | css=#add > .fa | 
driver.find_element(By.CSS_SELECTOR, "#add > .fa").click()
# 4 | doubleClick | css=.modal-backdrop | 
element = driver.find_element(By.CSS_SELECTOR, ".modal-backdrop")
actions = ActionChains(driver)
actions.double_click(element).perform()
# 5 | click | id=txtNombreGuion | 
driver.find_element(By.ID, "txtNombreGuion").click()
# 6 | click | id=txtNombreGuion | 
driver.find_element(By.ID, "txtNombreGuion").click()
# 7 | doubleClick | id=txtNombreGuion | 
element = driver.find_element(By.ID, "txtNombreGuion")
actions = ActionChains(driver)
actions.double_click(element).perform()
# 8 | type | id=txtNombreGuion | prueba sena
driver.find_element(By.ID, "txtNombreGuion").send_keys("prueba sena")
# 9 | click | id=guardarNewGuion | 
driver.find_element(By.ID, "guardarNewGuion").click()
# 10 | doubleClick | css=.blockOverlay | 
element = driver.find_element(By.CSS_SELECTOR, ".blockOverlay")
actions = ActionChains(driver)
actions.double_click(element).perform()