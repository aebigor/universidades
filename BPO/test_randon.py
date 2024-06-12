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
from PIL import Image
from io import BytesIO
import cv2
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
name.send_keys("senadyalogo@gmail.com")

# Busca el campo de contraseña
password = driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[2]/input')
password.send_keys("zkyOF0Fs")

# Hace clic en el botón de inicio de sesión
driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[3]/div[2]/button').click()

# Espera 2 segundos
time.sleep(2)

# Hace clic en el campo de huésped
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
#time.sleep(2)

# Entra en la sección de estrategias
driver.find_element(By.XPATH, "//li[@id='estrategias']/a/i").click()


driver.find_element(By.ID, "table_search_lista_navegacion").click()
driver.find_element(By.ID, "table_search_lista_navegacion").send_keys("laura")
driver.find_element(By.ID, "table_search_lista_navegacion").send_keys(Keys.ENTER) 
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#\\32 b036f4892dad21d0dedf3ecd5c94270 > td").click()
driver.implicitly_wait(2)
time.sleep(2)

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
pyautogui.move(600, 80, duration=1)
# Esperar 2 segundoss
time.sleep(2)
# Realizar un doble clic en la posición final
pyautogui.doubleClick()

driver.find_element(By.LINK_TEXT, 'CONFIGURACIÓN TEMAS TELEFONICOS').click()

# Mover el mouse a las nuevas coordenadas pyautogui.doubleClick(x=x_absolute +250, y=y_absolute -159, duration=1)
#pyautogui.move(200, 0, duration=2)
driver.find_element(By.ID, "G10_C330").click()
time.sleep(2)

driver.find_element(By.ID, "Save").click()

time.sleep(4)
# Soltar el botón del ratón
#pyautogui.mouseUp()
x_offset = 180   # ajusta según tus necesidades
y_offset = 150  # ajusta según tus necesidades

# Calcular las coordenadas absolutas dentro de la ventana del navegador
x_absolute = canvas_location['x'] + x_offset
y_absolute = canvas_location['y'] + y_offset

# Mover el mouse a las coordenadas absolutas y hacer clic
#pyautogui.moveTo(x_absolute, y_absolute, duration=1)
#pyautogui.mouseDown()
pyautogui.moveTo(x_absolute, y_absolute, duration=1)
pyautogui.move(600, 80, duration=1)
# Esperar 2 segundoss
time.sleep(2)
# Realizar un doble clic en la posición final
pyautogui.doubleClick()

# Esperar 1 segundo después de soltar
driver.find_element(By.LINK_TEXT, 'CONFIGURACIÓN TEMAS TELEFONICOS').click()

# Mover el mouse a las nuevas coordenadas pyautogui.doubleClick(x=x_absolute +250, y=y_absolute -159, duration=1)
#pyautogui.move(200, 0, duration=2)
driver.find_element(By.ID, "G10_C330").click()
time.sleep(2)
driver.find_element(By.ID, "ivr_encuesta").click()
    # 14 | select | id=ivr_encuesta | label=Pruebas_Bienvenida
dropdown = driver.find_element(By.ID, "ivr_encuesta")
dropdown.find_element(By.XPATH, "//option[. = 'Pruebas_Bienvenida']").click()

driver.find_element(By.ID, "ivr_encuesta").click()
    # 14 | select | id=ivr_encuesta | label=Pruebas_Bienvenida
dropdown = driver.find_element(By.ID, "ivr_encuesta")
dropdown.find_element(By.XPATH, "//option[. = 'IVR POR DEFECTO']").click()

time.sleep(2)
driver.find_element(By.ID, "Save").click()
#time.sleep(10)

# Realizar un doble clic en otras coordenadas 
# Realizar un clic en otras coordenadas 


# Esperar 10 segundos después de hacer clic
time.sleep(10)