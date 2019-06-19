# indeed.py
from time import sleep
from selenium import webdriver
# indica el browser
browser = webdriver.Chrome()
browser.implicitly_wait(15)

browser.get("https://www.indeed.nl/")

# indica que debe escribir la busqueda y hacer algo
form = browser.find_element_by_name("q")
form.send_keys("junior javascript developer")

# wait three seconds until submit
sleep(3)
form.submit()

# en la busqueda debe seleccionar con un click la oferta

jobad = browser.find_element_by_id('sja1')

# hago click sobre un aviso
print("hare click sobre un aviso")
sleep(3)
jobad.click()

# cambio hacia elemento activo
browser.switch_to_active_element()
# hago click sobre el boton solicitar
browser.find_element_by_class_name('indeed-apply-button-label').click()
sleep(3)


# sleep(10)
# browser.quit()
