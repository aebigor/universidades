from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd



# Configura las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo sin cabeza
chrome_options.add_argument("--disable-gpu") 
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.elempleo.com/colombia/Files/BasesUniversitarias/universidad-bosque/Home.aspx?ekp=4ylL1XxasTfttAUBYbQ2O8Q53xyOoS9yOGA4sBzeaMoGTMRtQ9JhAEv3Z3lWrzc5gDV2smXs/PX5nG1LskBC5PvagFAdsEwhlJc1icLyDM+IKFN8iH1S1hhAwZIfdf05X01l4fOXWEKtAW2RmZZn+QKJRFHDydFQlQ6ft9TThjU=")
driver.set_window_size(1382, 736)
# Ruta al archivo Excel con los datos
ruta_excel = './ofertas_de_empleo.xlsx'

# Cargar los datos desde el archivo Excel
df = pd.read_excel(ruta_excel)

# Inicializar el WebDriver (ChromeDriver en este ejemplo)



# Abrir la página web
driver.get(url)

# Iterar a través de cada fila en el DataFrame
for index, row in df.iterrows():
    # Ejemplo: llenar un campo de texto
    # Supongamos que el formulario tiene un campo con ID 'campo_texto' y debes llenarlo con el valor de 'campo_de_texto' en el DataFrame
    campo_texto = driver.find_element_by_id('campo_texto')
    campo_texto.send_keys(row['campo_de_texto'])

    # Ejemplo: seleccionar una opción de un campo de selección (select)
    # Supongamos que el formulario tiene un campo select con ID 'campo_select' y debes seleccionar la opción basada en el valor de 'campo_de_seleccion' en el DataFrame
    select_element = Select(driver.find_element_by_id('campo_select'))
    select_element.select_by_visible_text(row['campo_de_seleccion'])

    # Ejemplo: buscar y chulear (marcar) una casilla de verificación o radio button según la palabra clave
    # Supongamos que tienes un campo con ID 'campo_chulear' y quieres marcarlo si 'palabra_clave' en el DataFrame es 'Sí'
    if row['palabra_clave'] == 'Sí':
        campo_chulear = driver.find_element_by_id('campo_chulear')
        if not campo_chulear.is_selected():
            campo_chulear.click()
    
    # Continúa con los demás campos según sea necesario

# Una vez que hayas completado todo el proceso, cierra el navegador
driver.quit()
