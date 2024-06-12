
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
import numpy as np
import pyautogui

#abre gooogleCH
driver = webdriver.Chrome()
driver.get("https://qa.dyalogo.cloud/manager/login.php")
driver.set_window_size(1382, 736)

# Obtener el tamaño de la pantalla
screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

# Establecer el tamaño de la ventana del navegador
driver.set_window_size(screen_width, screen_height)

# Busca el campo de nombre de usuario
name = driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[1]/input')
name.send_keys("santicri163@gmail.com")

# Busca el campo de contraseña
password = driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[2]/input')
password.send_keys("JaaeGyfF")

# Hace clic en el botón de inicio de sesión
driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[3]/div[2]/button').click()

# Espera 2 segundos
time.sleep(2)
#
##Hace clic en el campo de huésped
#driver.find_element("xpath", '//*[@id="PonerHuesped"]/div/div/form/div[2]/div/span/span[1]/span').click()
#
## Selecciona el campo para buscar
#Huesped = driver.find_element("xpath", '/html/body/span/span/span[1]/input')
#Huesped.send_keys("SENA KIDS", Keys.ENTER)
#
## Hace clic en el botón de guardar
#driver.find_element("xpath", '//*[@id="btnGuardar"]').click()
#
## Espera 2 segundos
time.sleep(2)

# Entra en la sección de estrategias
driver.find_element(By.XPATH, "//li[@id='estrategias']/a/i").click()


driver.find_element(By.ID, "table_search_lista_navegacion").click()
driver.find_element(By.ID, "table_search_lista_navegacion").send_keys("laura")
driver.find_element(By.ID, "table_search_lista_navegacion").send_keys(Keys.ENTER) 
time.sleep(10)
#driver.find_element(By.CSS_SELECTOR, "#\\32 b036f4892dad21d0dedf3ecd5c94270 > td").click()
driver.implicitly_wait(2)
time.sleep(10)

driver.find_element(By.CSS_SELECTOR, ".fa-edit").click()

driver.find_element(By.CSS_SELECTOR, ".ion").click()



# Canvas

# Esperar hasta 10 segundos hasta que aparezca el elemento canvas
canvas_selector = '#myDiagramDiv > canvas'
canvas_element = driver.find_element(By.CSS_SELECTOR, canvas_selector)

# Obtener la posición del elemento canvas
canvas_location = canvas_element.location

# Calcular la posición relativa dentro del canvas donde deseas hacer clic
x_offset = 180   # ajusta según tus necesidades
y_offset = 150  # ajusta según tus necesidades

# Calcular las coordenadas absolutas dentro de la ventana del navegador
x_absolute = canvas_location['x'] + x_offset
y_absolute = canvas_location['y'] + y_offset

# Mover el mouse a las coordenadas absolutas y hacer clic
#pyautogui.moveTo(x_absolute, y_absolute, duration=1)
#pyautogui.mouseDown()
pyautogui.moveTo(x_absolute, y_absolute, duration=1)
pyautogui.move(90, 95, duration=2)
# Esperar 2 segundoss
time.sleep(2)
# Realizar un doble clic en la posición final
pyautogui.doubleClick()

# Mover el mouse a las nuevas coordenadas pyautogui.doubleClick(x=x_absolute +250, y=y_absolute -159, duration=1)
#pyautogui.move(200, 0, duration=2)

# Soltar el botón del ratón
#pyautogui.mouseUp()

# Esperar 1 segundo después de soltar
#time.sleep(10)

# Realizar un doble clic en otras coordenadas 
# Realizar un clic en otras coordenadas 


# Esperar 10 segundos después de hacer clic
time.sleep(10)

driver.find_element(By.ID, "estconActivo").click()
driver.find_element(By.ID, "btnSaveFiltros").click()
element = driver.find_element(By.ID, "btnSaveFiltros")
time.sleep(5)


# Calcular la posición relativa dentro del canvas donde deseas hacer clic
x_offset = 180   # ajusta según tus necesidades
y_offset = 150  # ajusta según tus necesidades

# Calcular las coordenadas absolutas dentro de la ventana del navegador
x_absolute = canvas_location['x'] + x_offset
y_absolute = canvas_location['y'] + y_offset

# Mover el mouse a las coordenadas absolutas y hacer clic
#pyautogui.moveTo(x_absolute, y_absolute, duration=1)
#pyautogui.mouseDown()
pyautogui.moveTo(x_absolute, y_absolute, duration=1)
pyautogui.move(90, 95, duration=2)
# Esperar 2 segundoss
time.sleep(2)
# Realizar un doble clic en la posición final
pyautogui.doubleClick()
driver.find_element(By.ID, "estconActivo").click()
time.sleep(5)
driver.find_element(By.ID, "radiocondiciones3").click()
time.sleep(5)
driver.find_element(By.ID, "radiocondiciones1").click()
time.sleep(5)
driver.find_element(By.ID, "radiocondiciones3").click()
time.sleep(5)
driver.find_element(By.ID, "newFiltro").click()
element = driver.find_element(By.ID, "newFiltro")
time.sleep(5)

actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)

driver.find_element(By.ID, "newFiltro").click()
time.sleep(2)

#element = driver.find_element(By.ID, "newFiltro")
#time.sleep(2)

actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)


""" try:   
    Select = driver.find_element(By.ID, '//*[@id="cmbTipoInsercion"]')
except: """

#Select


#para que registros aplica

Select = driver.find_element(By.XPATH, '//*[@id="condiciones_1"]')
Select.click()
Option= driver.find_element(By.XPATH,"//option[@value='(']")

Option.click()
time.sleep(2)


Select = driver.find_element(By.XPATH, '//*[@id="pregun_1"]')
Select.click()
Option= driver.find_element(By.XPATH,'//*[@id="pregun_1"]/option[11]')
Option.click()
time.sleep(4)

Select = driver.find_element(By.XPATH, '/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/select')
Select.click()
Option= driver.find_element(By.XPATH,"/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/select/option")
Option.click()
time.sleep(2)

Select = driver.find_element(By.XPATH, '//*[@id="valor_1"]')
Select.click()
Option= driver.find_element(By.XPATH,"/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[1]/div[4]/div/select/option[2]")
Option.click()
time.sleep(2)

Select = driver.find_element(By.XPATH, '//*[@id="cierre1"]')
Select.click()
Option= driver.find_element(By.XPATH,'//*[@id="cierre1"]/option[2]')
Option.click()
time.sleep(2)

try:
    Select = driver.find_element(By.XPATH, '//*[@id="condiciones_2"]')

    Select.click()
    Option= driver.find_element(By.XPATH,"/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/select/option[1]")
    Option.click()
except:
    Select = driver.find_element(By.XPATH, '/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/select')
    Select.click()
    Option= driver.find_element(By.XPATH,"//option[@value='&']")
    Option.click()

Select = driver.find_element(By.XPATH, '//*[@id="pregun_2"]')
Select.click()
Option= driver.find_element(By.XPATH,'/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/select/option[2]')
Option.click()
time.sleep(2)

Select = driver.find_element(By.XPATH, '//*[@id="condicion_2"]')
Select.click()
Option= driver.find_element(By.XPATH,'/html/body/div[7]/div[6]/div[14]/div/div/div[2]/form/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/select/option[2]')
Option.click()
time.sleep(2)

Select = driver.find_element(By.XPATH, '//*[@id="cierre2"]')
Select.click()
Option= driver.find_element(By.XPATH,'//*[@id="cierre2"]/option[2]')
Option.click()
time.sleep(2)

driver.find_element(By.ID, "valor_2").click()
# 36 | type | id=valor_2 | 1
driver.find_element(By.ID, "valor_2").send_keys("1")
# 37 | sendKeys | id=valor_2 | ${KEY_ENTER}
driver.find_element(By.ID, "valor_2").send_keys(Keys.ENTER)

driver.find_element(By.ID, "radiocondiciones1").click()


#CUANDO REALIZAR LA ACTIVIDAD


Select = driver.find_element(By.XPATH, '//*[@id="cmbTipoInsercion"]')
Select.click()
#Option
Option= driver.find_element(By.XPATH,"//option[@value='-1']")
Select.click()
time.sleep(2)

Select = driver.find_element(By.XPATH, '//*[@id="cmbTipoInsercion"]')
Select.click()
#Option
Option= driver.find_element(By.XPATH,"//option[@value='0']")
Select.click()
time.sleep(2)



driver.find_element(By.ID, "cmbCampoFecha").click()
dropdown = driver.find_element(By.ID, "cmbCampoFecha")
dropdown.find_element(By.XPATH, "//option[. = 'Hoy']").click()
driver.find_element(By.ID, "masMenosFecha").click()
dropdown = driver.find_element(By.ID, "masMenosFecha")
dropdown.find_element(By.XPATH, "//option[. = 'Menos']").click()
driver.find_element(By.ID, "txtRestaSumaFecha").click()
driver.find_element(By.ID, "txtRestaSumaFecha").send_keys("01")
driver.find_element(By.ID, "cmbCampoHora").click()
driver.find_element(By.ID, "masMenosHora").click()
dropdown = driver.find_element(By.ID, "masMenosHora")
dropdown.find_element(By.XPATH, "//option[. = 'Menos']").click()
driver.find_element(By.ID, "txtRestaSumaHora").click()
driver.find_element(By.ID, "txtRestaSumaHora").send_keys("2")
driver.find_element(By.ID, "sacarPasoAnterior").click()
driver.find_element(By.ID, "sacarPasoAnterior").click()
driver.find_element(By.ID, "sacarOtrosPasos").click()
driver.find_element(By.ID, "resucitarRegistros").click()
driver.find_element(By.ID, "resucitarRegistros").click()
time.sleep(5)


actions.double_click(element).perform()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".select2-selection--multiple > .select2-selection__rendered").click()
time.sleep(5)
driver.find_element(By.ID, "sacarOtrosPasos").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".select2-selection--multiple > .select2-selection__rendered").click()
time.sleep(5)


driver.find_element(By.ID, "sacarOtrosPasos").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".select2-selection--multiple > .select2-selection__rendered").click()
driver.find_element(By.CSS_SELECTOR, "#s_3 .col-md-6").click()
driver.find_element(By.ID, "btnSaveFiltros").click()
element = driver.find_element(By.ID, "btnSaveFiltros")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)

time.sleep(10)
# Comentar o eliminar la línea siguiente para que la página no se cierre automáticamente
driver.quit()
