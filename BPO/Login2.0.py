
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
from io import BytesIO<
import cv2
import numpy as np
import pyautogui

#abre gooogleCH
driver = webdriver.Chrome()
driver.get("https://qa.dyalogo.cloud/manager/login.php")
driver.set_window_size(1382, 736)

#look for input for name

name = driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[1]/input')
name.send_keys("senadyalogo@gmail.com")


#look for input for password
password = driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[2]/input')
password.send_keys("zkyOF0Fs")

driver.find_element("xpath", '//*[@id="Login"]/div[2]/form/div[3]/div[2]/button').click()

#wair 2 secod

#le da clic a el huesped
#driver.find_element("xpath", '//*[@id="PonerHuesped"]/div/div/form/div[2]/div/span/span[1]/span').click()
#ya seleciona el campo para busca
#Huesped = driver.find_element("xpath", '/html/body/span/span/span[1]/input')
#escribe el nombre y da enter
#Huesped.send_keys("SENA KIDS", Keys.ENTER)

#dar click en entrar

#driver.find_element("xpath", '//*[@id="btnGuardar"]').click()

#wair 2 secods
time.sleep(2)

driver.find_element("xpath", '/html/body/div[7]/header/nav/div/ul/li/a/span')


#entra a estrategia
driver.find_element(By.XPATH, "//li[@id='estrategias']/a/i").click()

driver.find_element(By.ID, "table_search_lista_navegacion").click()
driver.find_element(By.ID, "table_search_lista_navegacion").send_keys("laura")
driver.find_element(By.ID, "table_search_lista_navegacion").send_keys(Keys.ENTER) 
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "#\\32 b036f4892dad21d0dedf3ecd5c94270 > td").click()
driver.implicitly_wait(2)
time.sleep(10)

driver.find_element(By.CSS_SELECTOR, ".fa-edit").click()

driver.find_element(By.CSS_SELECTOR, ".ion").click()


#canvas

# Encontrar el elemento canvas
# Esperar a que el canvas esté presente
canvas_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#myDiagramDiv canvas"))
)

# Obtener la captura de pantalla del canvas
canvas_screenshot = canvas_element.screenshot_as_png
canvas_image = Image.open(BytesIO(canvas_screenshot))

# Convertir la imagen a formato OpenCV y escala de grises
canvas_image_np = np.array(canvas_image)
canvas_image_cv = cv2.cvtColor(canvas_image_np, cv2.COLOR_RGBA2GRAY)

# Convertir el color de la flecha a buscar a formato OpenCV (escala de grises)
arrow_color = (0, 0, 0)  # Flecha negra
arrow_color_cv = np.array([arrow_color], dtype=np.uint8)

# Buscar la flecha en la imagen del canvas
match_result = cv2.matchTemplate(canvas_image_cv, arrow_color_cv, cv2.TM_CCOEFF_NORMED)

# Calcular el valor máximo de la comparación de plantillas
max_val = np.max(match_result)

# Verificar si el valor máximo supera el umbral
if max_val > 0.8:  # Ajusta el umbral según sea necesario
    # Realizar acciones si se cumple la condición
    print("La flecha fue encontrada con un alto grado de similitud.")
else:
    print("La flecha no fue encontrada o la similitud es baja.")

time.sleep(10)


pyautogui.doubleClick()
    # Buscar flechas en el flujograma

# Buscar flechas en el flujograma
#black_arrow_positions = find_arrows(canvas_image, black_arrow_color)
#print("Black Arrow Positions:", black_arrow_positions)
## Resto del código...
#
## Interactuar con las flechas encontradas
#action = ActionChains(driver)
#
#for position in black_arrow_positions:
#    # Interactuar con la flecha negra en la posición dada
#    arrow_element = driver.find_element(By.CSS_SELECTOR, "#myDiagramDiv canvas")
#    action.move_to_element_with_offset(arrow_element, position[0], position[1]).click().perform()
#    # Agregar una pausa opcional para observar la interacción
#    time.sleep(2)
#
#for position in blue_arrow_positions:
#    # Interactuar con la flecha azul en la posición dada
#    arrow_element = driver.find_element(By.CSS_SELECTOR, "#myDiagramDiv canvas")
#    action.move_to_element_with_offset(arrow_element, position[0], position[1]).click().perform()
#    # Agregar una pausa opcional para observar la interacción
#    time.sleep(2)
#
#for position in gray_arrow_positions:
#    # Interactuar con la flecha gris en la posición dada
#    arrow_element = driver.find_element(By.CSS_SELECTOR, "#myDiagramDiv canvas")
#    action.move_to_element_with_offset(arrow_element, position[0], position[1]).click().perform()
#    # Agregar una pausa opcional para observar la interacción
time.sleep(20)
## Cerrar el navegador al finalizar
driver.quit()