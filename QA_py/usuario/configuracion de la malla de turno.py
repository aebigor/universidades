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
# Test name: CP06.1
# Step # | name | target | value
# 1 | open | https://qa.dyalogo.cloud/manager/modulo/usuarios | 
driver.get("https://qa.dyalogo.cloud/manager/modulo/usuarios")
# 2 | setWindowSize | 1004x708 | 
driver.set_window_size(1382, 736)
# 22 | click | name=txtUsuario | 
driver.find_element(By.NAME, "txtUsuario").click()
# 23 | type | name=txtUsuario | pluisanys@gmail.com
driver.find_element(By.NAME, "txtUsuario").send_keys("pluisanys@gmail.com")
# 24 | click | name=txtPassword | 
driver.find_element(By.NAME, "txtPassword").click()
# 25 | click | css=.iCheck-helper | 
driver.find_element(By.CSS_SELECTOR, ".iCheck-helper").click()
# 26 | type | name=txtPassword | ZVG14qxy
driver.find_element(By.NAME, "txtPassword").send_keys("ZVG14qxy")
# 27 | click | css=.col-xs-4 > .btn | 
driver.find_element(By.CSS_SELECTOR, ".col-xs-4 > .btn").click()
time.sleep(3)
# 3 | click | css=#add > .fa | 
driver.get("https://qa.dyalogo.cloud/manager/modulo/usuarios")
    # Step # | name | target | value
# 1 | open | https://qa.dyalogo.cloud/manager/modulo/usuarios 
# 3 | click | id=edit | 
driver.find_element(By.ID, "edit").click()
# 4 | click | id=select2-malla_turno-container | 
driver.find_element(By.ID, "select2-malla_turno-container").click()
# 5 | type | css=.select2-search__field | prueba 2
driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("prueba 2")
# 6 | sendKeys | css=.select2-search__field | ${KEY_ENTER}
driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)
# 7 | click | id=breakselect1 | 
driver.find_element(By.ID, "breakselect1").click()
# 8 | click | id=breakselect2 | 
driver.find_element(By.ID, "breakselect2").click()
# 9 | click | id=breakselect3 | 
driver.find_element(By.ID, "breakselect3").click()
# 10 | click | id=HorIniLun | 
driver.find_element(By.ID, "HorIniLun").click()
# 11 | click | css=.ui-timepicker-selected | 
driver.find_element(By.CSS_SELECTOR, ".ui-timepicker-selected").click()
# 12 | click | id=HorIniMie | 
driver.find_element(By.ID, "HorIniMie").click()
# 13 | doubleClick | id=HorIniSab | 
element = driver.find_element(By.ID, "HorIniSab")
actions = ActionChains(driver)
actions.double_click(element).perform()
# 14 | doubleClick | id=HorIniVie | 
element = driver.find_element(By.ID, "HorIniVie")
actions = ActionChains(driver)
actions.double_click(element).perform()
time.sleep(3)

# 17 | click | id=breakHorIniVie1 | 

# 18 | click | css=.ui-timepicker-selected:nth-child(111) | 
driver.find_element(By.ID, "breakHorIniLun1").click()
time.sleep(3)
driver.find_element(By.ID, "breakHorIniLun1").click()
# 19 | click | id=breakHorIniMie1 | 
driver.find_element(By.ID, "breakHorIniSab1").click()
# 20 | click | css=.table-responsive tr:nth-child(7) > td:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".table-responsive tr:nth-child(7) > td:nth-child(3)").click()
# 21 | click | id=breakHorIniMar1 | 
driver.find_element(By.ID, "breakHorIniMar1").click()
# 22 | click | css=.table-responsive tr:nth-child(4) > td:nth-child(4) | 
# 23 | mouseDown | id=breakHorFinJue1 | 
element = driver.find_element(By.ID, "breakHorFinJue1")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
# 24 | click | css=.skin-blue | 
driver.find_element(By.CSS_SELECTOR, ".skin-blue").click()
# 25 | click | id=breakHorFinVie1 | 
driver.find_element(By.ID, "breakHorFinVie1").click()
# 26 | click | id=breakHorFinMar2 | 
driver.find_element(By.ID, "breakHorFinMar2").click()
# 27 | click | id=breakHorFinJue2 | 
driver.find_element(By.ID, "breakHorFinJue1").click()
# 28 | click | id=breakHorIniJue3 | 
driver.find_element(By.ID, "breakHorIniJue3").click()
# 29 | click | linkText=OTRAS PAUSAS CON HORARIO | 
driver.find_element(By.LINK_TEXT, "OTRAS PAUSAS CON HORARIO").click()
# 30 | click | id=agregarHorarioFijo1 | 
driver.find_element(By.ID, "agregarHorarioFijo1").click()
# 31 | click | name=selectTipo1[] | 

# 32 | click | id=PHorIniLun4614 | driver.find_element(By.ID, "PHorIniLun4614").click()
# 33 | click | id=PHorFinLun4614 | driver.find_element(By.ID, "PHorFinLun4614").click()
# 34 | click | css=#FormularioDatos | 
driver.find_element(By.CSS_SELECTOR, "#FormularioDatos").click()
# 35 | click | css=.btn:nth-child(1) > .fa-trash | 
driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1) > .fa-trash").click()
time.sleep(3)
# 36 | click | linkText=PAUSAS SIN HORARIO | 
driver.find_element(By.LINK_TEXT, "PAUSAS SIN HORARIO").click()
# 37 | click | id=agregarHorarioFijo0 | 
driver.find_element(By.ID, "agregarHorarioFijo0").click()
time.sleep(3)
# 38 | click | name=selectTipo0[] | 
driver.find_element(By.NAME, "selectTipo0[]").click()
# 39 | type | name=selectTipo0[] | label=Descanso
driver.find_element(By.NAME, "selectTipo0[]").send_keys("label=Baño")
time.sleep(3)
# 40 | click | id=PCLun4628 | 

# 41 | click | id=PCLun4615 | driver.find_element(By.ID, "PCLun4615").click()
# 46 | click | id=agregarHorarioFijo0 | driver.find_element(By.ID, "agregarHorarioFijo0").click()
# 47 | click | id=fila4616 | driver.find_element(By.ID, "fila4616").click()
# 48 | runScript | window.scrollTo(0,400) | 
driver.execute_script("window.scrollTo(0,400)")
