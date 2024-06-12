import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuzzywuzzy import fuzz, process

# Carga el archivo de Excel
excel_path = './ofertas_de_empleo.xlsx'  # Reemplaza con la ruta a tu archivo de Excel
df = pd.read_excel(excel_path)

# Inicializa el navegador web
driver = webdriver.Chrome()

# Navega a la página webdriver
url = 'https://www.elempleo.com/colombia/Files/BasesUniversitarias/u_militar/Home.aspx'
driver.get(url)

# Realiza el inicio de sesión
username = 'desarrollador-junior@yo-soy.co'
password = '900299250'

driver.find_element(By.ID, 'ctl00_Header1_UniversityCompaniesControl_headerLoginControl_txtUserName').send_keys(username)
driver.find_element(By.ID, 'ctl00_Header1_UniversityCompaniesControl_headerLoginControl_txtPassword').send_keys(password)
driver.find_element(By.ID, 'ctl00_Header1_UniversityCompaniesControl_headerLoginControl_btnLogin').click()

driver.find_element(By.ID, "ctl00_content_PublishJobOfferButton").click()

for index, row in df.iterrows():
    # Completa el título
    campo1 = driver.find_element(By.ID, 'ctl00_content_ctl73_title')
    campo1.clear()
    campo1.send_keys(row.iloc[0])

    # Define la palabra clave y otros parámetros iniciales
    palabra_clave = row.iloc[1].strip().lower()
    umbral_similitud = 80
    intentos = 0
    opcion_seleccionada = None

    # Continúa intentando mientras no se encuentre la opción y los intentos sean menores a 5
    while opcion_seleccionada is None and intentos < 5:
        try:
            # Espera a que los contenedores de opciones estén disponibles
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'checkboxlist-container')))
            contenedores = driver.find_elements(By.CLASS_NAME, 'checkboxlist-container')

            for contenedor in contenedores:
                opciones_input = contenedor.find_elements(By.XPATH, './/input[@type="checkbox"]')
                for input_checkbox in opciones_input:
                    texto_opcion = input_checkbox.find_element(By.XPATH, './following-sibling::label').text.strip().lower()
                    similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                    if similitud >= umbral_similitud:
                        input_checkbox.click()
                        opcion_seleccionada = texto_opcion
                        print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                        break
                if opcion_seleccionada:
                    break
        except Exception as e:
            print(f"Error al buscar opciones: {e}")

        intentos += 1
        if opcion_seleccionada is None:
            time.sleep(2)  # Espera antes de intentar nuevamente

    if opcion_seleccionada is None:
        print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")
    # Verifica si el valor de la columna C-2 es 'sí' utilizando iloc para acceder a la posición 2

    palabra_clave = row.iloc[2].strip().lower()
    umbral_similitud = 80
    intentos = 0
    opcion_seleccionada = None

    while opcion_seleccionada is None and intentos < 5:
        try:
            # Espera a que los contenedores de opciones estén disponibles
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'checkboxlist-container')))
            contenedores = driver.find_elements(By.CLASS_NAME, 'checkboxlist-container')

            for contenedor in contenedores:
                opciones_input = contenedor.find_elements(By.XPATH, './/input[@type="checkbox"]')
                for input_checkbox in opciones_input:
                    texto_opcion = input_checkbox.find_element(By.XPATH, './following-sibling::label').text.strip().lower()
                    similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                    if similitud >= umbral_similitud:
                        input_checkbox.click()
                        opcion_seleccionada = texto_opcion
                        print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                        break
                if opcion_seleccionada:
                    break
        except Exception as e:
            print(f"Error al buscar opciones: {e}")

        intentos += 1
        if opcion_seleccionada is None:
            time.sleep(2)  # Espera antes de intentar nuevamente

    if opcion_seleccionada is None:
        print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")

    palabra_clave_select = row.iloc[3].strip()
    print(f"Palabra clave del select obtenida de la hoja de cálculo: '{palabra_clave_select}'")
    select = driver.find_element(By.ID, 'ctl00_content_ctl73_positionLevel')
    select.click()  
    time.sleep(1)
    opciones_select = select.find_elements(By.TAG_NAME, 'option')
    for opcion in opciones_select:
      opcion_texto = opcion.text.strip()
      print(f"Valor de la opción encontrada: '{opcion_texto}'")
      if opcion_texto == palabra_clave_select:
          opcion.click()  # Seleccionar la opción
          print(f"Valor del select '{palabra_clave_select}' seleccionado.")
          break
    time.sleep(3)
    palabra_clave_select = row.iloc[4].strip()
    print(f"Palabra clave del select obtenida de la hoja de cálculo: '{palabra_clave_select}'")
    select = driver.find_element(By.ID, 'ctl00_content_ctl73_positionSubLevel')
    select.click()  
    time.sleep(1)
    opciones_select = select.find_elements(By.TAG_NAME, 'option')
    for opcion in opciones_select:
      opcion_texto = opcion.text.strip()
      print(f"Valor de la opción encontrada: '{opcion_texto}'")
      if opcion_texto == palabra_clave_select:
          opcion.click()  # Seleccionar la opción
          print(f"Valor del select '{palabra_clave_select}' seleccionado.")
          break

   


    # Completa el título
campo2 = driver.find_element(By.ID, 'ctl00_content_ctl73_field_JobOffer_AdditionalInfo_VacancyQuantity_box')
campo2.clear()
campo2.send_keys(row.iloc[5])

palabra_clave_select = row.iloc[6].strip()
print(f"Palabra clave del select obtenida de la hoja de cálculo: '{palabra_clave_select}'")
select = driver.find_element(By.ID, 'ctl00_content_ctl73_field_JobOffer_Salary_SalaryInfo_box')
select.click()  
time.sleep(1)
opciones_select = select.find_elements(By.TAG_NAME, 'option')
for opcion in opciones_select:
      opcion_texto = opcion.text.strip()
      print(f"Valor de la opción encontrada: '{opcion_texto}'")
      if opcion_texto == palabra_clave_select:
          opcion.click()  # Seleccionar la opción
          print(f"Valor del select '{palabra_clave_select}' seleccionado.")
          



for index, row in df.iterrows():
    # Completa el título
    campo1 = driver.find_element(By.ID, 'ctl00_content_ctl74_descriptionBox_text')
    campo1.clear()
    campo1.send_keys(row.iloc[7])   
    # Verifica si el valor de la columna C-2 es 'sí' utilizando iloc para acceder a la posición 2

for index, row in df.iterrows():
    # Completa el título
    campo1 = driver.find_element(By.ID, 'ctl00_content_ctl74_requirements_text')
    campo1.clear()
    campo1.send_keys(row.iloc[8])

    palabra_clave = str(row.iloc[9]).lower()

    umbral_similitud = 80
    intentos = 0
    opcion_seleccionada = None

while opcion_seleccionada is None and intentos < 5:
    try:
        # Espera a que los contenedores de opciones estén disponibles
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'checkboxlist-container')))
        contenedores = driver.find_elements(By.CLASS_NAME, 'checkboxlist-container')

        for contenedor in contenedores:
            # Busca los spans que contienen los inputs de tipo radio
            opciones_radio = contenedor.find_elements(By.XPATH, ".//span[contains(@id, 'ctl')]/input[@type='radio']")
            for input_radio in opciones_radio:
                # Puedes obtener el texto del label asociado si es necesario
                label = input_radio.find_element(By.XPATH, './following-sibling::label')
                texto_opcion = label.text.strip().lower()
                similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                if similitud >= umbral_similitud:
                    input_radio.click()  # Hacemos clic en el radio button
                    opcion_seleccionada = texto_opcion
                    print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                    break
            if opcion_seleccionada:
                break
    except Exception as e:
        print(f"Error al buscar opciones: {e}")

    intentos += 1
    if opcion_seleccionada is None:
        time.sleep(2)  # Espera antes de intentar nuevamente

if opcion_seleccionada is None:
    print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")



palabra_clave = row.iloc[10].strip().lower()
umbral_similitud = 80
intentos = 0
opcion_seleccionada = None

while opcion_seleccionada is None and intentos < 5:
        try:
            # Espera a que los contenedores de opciones estén disponibles
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'checkboxlist-container')))
            contenedores = driver.find_elements(By.CLASS_NAME, 'checkboxlist-container')

            for contenedor in contenedores:
                opciones_input = contenedor.find_elements(By.XPATH, './/input[@type="checkbox"]')
                for input_checkbox in opciones_input:
                    texto_opcion = input_checkbox.find_element(By.XPATH, './following-sibling::label').text.strip().lower()
                    similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                    if similitud >= umbral_similitud:
                        input_checkbox.click()
                        opcion_seleccionada = texto_opcion
                        print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                        break
                if opcion_seleccionada:
                    break
        except Exception as e:
            print(f"Error al buscar opciones: {e}")

        intentos += 1
        if opcion_seleccionada is None:
            time.sleep(2)  # Espera antes de intentar nuevamente

if opcion_seleccionada is None:
        print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")


palabra_clave = str(row.iloc[11]).lower()

umbral_similitud = 80
intentos = 0
opcion_seleccionada = None

while opcion_seleccionada is None and intentos < 5:
    try:
        # Espera a que los contenedores de opciones estén disponibles
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'checkboxlist-container')))
        contenedores = driver.find_elements(By.CLASS_NAME, 'checkboxlist-container')

        for contenedor in contenedores:
            # Busca los spans que contienen los inputs de tipo radio
            opciones_radio = contenedor.find_elements(By.XPATH, ".//span[contains(@id, 'ctl')]/input[@type='radio']")
            for input_radio in opciones_radio:
                # Puedes obtener el texto del label asociado si es necesario
                label = input_radio.find_element(By.XPATH, './following-sibling::label')
                texto_opcion = label.text.strip().lower()
                similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                if similitud >= umbral_similitud:
                    input_radio.click()  # Hacemos clic en el radio button
                    opcion_seleccionada = texto_opcion
                    print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                    break
            if opcion_seleccionada:
                break
    except Exception as e:
        print(f"Error al buscar opciones: {e}")

    intentos += 1
    if opcion_seleccionada is None:
        time.sleep(2)  # Espera antes de intentar nuevamente

if opcion_seleccionada is None:
    print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")


palabra_clave = row.iloc[12].strip().lower()
umbral_similitud = 80
intentos = 0
opcion_seleccionada = None

while opcion_seleccionada is None and intentos < 5:
        try:
            # Espera a que los contenedores de opciones estén disponibles
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'ctl00_content_ctl76_sectors_childList')))
            contenedores = driver.find_elements(By.ID, 'ctl00_content_ctl76_sectors_childList')

            for contenedor in contenedores:
                opciones_input = contenedor.find_elements(By.XPATH, './/input[@type="checkbox"]')
                for input_checkbox in opciones_input:
                    texto_opcion = input_checkbox.find_element(By.XPATH, './following-sibling::label').text.strip().lower()
                    similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                    if similitud >= umbral_similitud:
                        input_checkbox.click()
                        opcion_seleccionada = texto_opcion
                        print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                        break
                if opcion_seleccionada:
                    break
        except Exception as e:
            print(f"Error al buscar opciones: {e}")

        intentos += 1
        if opcion_seleccionada is None:
            time.sleep(2)  # Espera antes de intentar nuevamente

if opcion_seleccionada is None:
        print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")

palabra_clave = str(row.iloc[13]).lower()

umbral_similitud = 80
intentos = 0
opcion_seleccionada = None

while opcion_seleccionada is None and intentos < 5:
    try:
        # Espera a que los contenedores de opciones estén disponibles
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'checkboxlist-container')))
        contenedores = driver.find_elements(By.CLASS_NAME, 'checkboxlist-container')

        for contenedor in contenedores:
            # Busca los spans que contienen los inputs de tipo radio
            opciones_radio = contenedor.find_elements(By.XPATH, ".//span[contains(@id, 'ctl')]/input[@type='radio']")
            for input_radio in opciones_radio:
                # Puedes obtener el texto del label asociado si es necesario
                label = input_radio.find_element(By.XPATH, './following-sibling::label')
                texto_opcion = label.text.strip().lower()
                similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                if similitud >= umbral_similitud:
                    input_radio.click()  # Hacemos clic en el radio button
                    opcion_seleccionada = texto_opcion
                    print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                    break
            if opcion_seleccionada:
                break
    except Exception as e:
        print(f"Error al buscar opciones: {e}")

    intentos += 1
    if opcion_seleccionada is None:
        time.sleep(2)  # Espera antes de intentar nuevamente

if opcion_seleccionada is None:
    print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")



palabra_clave = row.iloc[14].strip().lower()
umbral_similitud = 100
intentos = 0
opcion_seleccionada = None

while opcion_seleccionada is None and intentos < 5:
        try:
            # Espera a que los contenedores de opciones estén disponibles
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'ctl00_content_ctl77_checkBoxList')))
            contenedores = driver.find_elements(By.ID, 'ctl00_content_ctl77_checkBoxList')

            for contenedor in contenedores:
                opciones_input = contenedor.find_elements(By.XPATH, './/input[@type="checkbox"]')
                for input_checkbox in opciones_input:
                    texto_opcion = input_checkbox.find_element(By.XPATH, './following-sibling::label').text.strip().lower()
                    similitud = fuzz.partial_ratio(palabra_clave, texto_opcion)
                    if similitud >= umbral_similitud:
                        input_checkbox.click()
                        opcion_seleccionada = texto_opcion
                        print(f"Opción seleccionada: {opcion_seleccionada} para la palabra clave {palabra_clave}")
                        break
                if opcion_seleccionada:
                    break
        except Exception as e:
            print(f"Error al buscar opciones: {e}")

        intentos += 1
        if opcion_seleccionada is None:
            time.sleep(2)  # Espera antes de intentar nuevamente

if opcion_seleccionada is None:
        print(f"No se encontró una opción adecuada para '{palabra_clave}' tras {intentos} intentos.")



for index, row in df.iterrows():
    # Completa el título
    campo1 = driver.find_element(By.ID, 'ctl00_content_ctl78_fromExperienceYears')
    campo1.clear()
    campo1.send_keys(row.iloc[15])

for index, row in df.iterrows():
    # Completa el título
    campo1 = driver.find_element(By.ID, 'ctl00_content_ctl78_toExperienceYeras')
    campo1.clear()
    campo1.send_keys(row.iloc[16])

palabra_clave_select = str(row.iloc[17]).strip()
print(f"Tipo de dato: {type(row.iloc[17])}, Valor: {row.iloc[17]}")
select = driver.find_element(By.ID, 'ctl00_content_ctl78_field_JobOffer_AdditionalInfo_RequiredExperience_box')
select.click()  
time.sleep(1)
opciones_select = select.find_elements(By.TAG_NAME, 'option')
for opcion in opciones_select:
      opcion_texto = opcion.text.strip()
      print(f"Valor de la opción encontrada: '{opcion_texto}'")
      if opcion_texto == palabra_clave_select:
          opcion.click()  # Seleccionar la opción
          print(f"Valor del select '{palabra_clave_select}' seleccionado.")

palabra_clave_select = row.iloc[18].strip()
print(f"Palabra clave del select obtenida de la hoja de cálculo: '{palabra_clave_select}'")
select = driver.find_element(By.ID, 'ctl00_content_ctl78_field_JobOffer_AdditionalInfo_ContractType_box')
select.click()  
time.sleep(1)
opciones_select = select.find_elements(By.TAG_NAME, 'option')
for opcion in opciones_select:
      opcion_texto = opcion.text.strip()
      print(f"Valor de la opción encontrada: '{opcion_texto}'")
      if opcion_texto == palabra_clave_select:
          opcion.click()  # Seleccionar la opción
          print(f"Valor del select '{palabra_clave_select}' seleccionado.")

palabra_clave_select = row.iloc[19].strip()
print(f"Palabra clave del select obtenida de la hoja de cálculo: '{palabra_clave_select}'")
select = driver.find_element(By.ID, 'ctl00_content_ctl78_field_JobOffer_AdditionalInfo_DedicatedTime_box')
select.click()  
time.sleep(1)
opciones_select = select.find_elements(By.TAG_NAME, 'option')
for opcion in opciones_select:
      opcion_texto = opcion.text.strip()
      print(f"Valor de la opción encontrada: '{opcion_texto}'")
      if opcion_texto == palabra_clave_select:
          opcion.click()  # Seleccionar la opción
          print(f"Valor del select '{palabra_clave_select}' seleccionado.")

# fila_actual += 1
time.sleep(10)

boton = driver.find_element(By.ID, 'ctl00_content_ctl73_PublishCompanyNameNo')  # Reemplazar 'id_del_boton' con el ID real

# Hacer clic en el botón
boton.click()

boton = driver.find_element(By.ID, 'ctl00_content_ctl73_field_JobOffer_Salary_PublishSalary_box_list_1')  # Reemplazar 'id_del_boton' con el ID real

# Hacer clic en el botón
boton.click() 

boton = driver.find_element(By.ID, 'ctl00_content_ctl77_academyState_2')  # Reemplazar 'id_del_boton' con el ID real

# Hacer clic en el botón
boton.click()

boton = driver.find_element(By.ID, 'ctl00_content_Save')  # Reemplazar 'id_del_boton' con el ID real

# Hacer clic en el botón
boton.click()

boton = driver.find_element(By.ID, 'ctl00_content_Save_dialogContainerok_button')  # Reemplazar 'id_del_boton' con el ID real

# Hacer clic en el botón
boton.click()

time.sleep(10)

driver.quit()
