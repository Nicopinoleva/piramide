import os
import math
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



print('libs ok')

#pruebas
pruebas_aprobadas=[]
pruebas_reprobadas=[]
nombres = ["Pedro","juan","Diego","Bea","Nelson","MaxTurbo15"]

#driver
driver = webdriver.Chrome()


#ingresar pagina por chrome (2)
try:
	driver.get("http://181.43.143.136:2000/piramide/")
	pruebas_aprobadas.append('ingresar pagina por chrome')
except:
	pruebas_reprobadas.append('ingresar pagina por chrome')

time.sleep(3)



#Prueba nombre minuscula(1)

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("jugador Minuscula")
	driver.find_element_by_xpath("/html/body/div/div/div[1]/form/button").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Prueba nombre minuscula(1)')
else:
	pruebas_reprobadas.append('Prueba nombre minuscula(1)')

time.sleep(2)



#Prueba nombre Mayuscula(1) (por mouse)
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("JUGADOR MAYUSCULA")
	driver.find_element_by_xpath("/html/body/div/div/div[1]/form/button").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Prueba nombre Mayuscula(1) (por mouse)')
else:
	pruebas_reprobadas.append('Prueba nombre Mayuscula(1) (por mouse)')
time.sleep(2)



#prueba nombre numeros(1) (por mouse)
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("12354689")
	driver.find_element_by_xpath("/html/body/div/div/div[1]/form/button").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('prueba nombre numeros(1) (por mouse)')
else:
	pruebas_reprobadas.append('prueba nombre numeros(1) (por mouse)')
time.sleep(2)


#prueba nombre ALFANUMERICO(1) (por mouse)
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("M4T14S")
	driver.find_element_by_xpath("/html/body/div/div/div[1]/form/button").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('prueba nombre ALFANUMERICO(1) (por mouse)')
else:
	pruebas_reprobadas.append('prueba nombre ALFANUMERICO(1) (por mouse)')
time.sleep(2)



#Agregar Nombre por boton Enter
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("M4T14S",Keys.ENTER)

	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar Nombre por boton Enter')
else:
	pruebas_reprobadas.append('Agregar Nombre por boton Enter')
time.sleep(2)



#Mantener jugadores con Nombre al refrescar
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("M4T14S",Keys.ENTER)
	driver.get("http://181.43.143.136:2000/piramide/")
	time.sleep(2)
	nombre = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div").text
	if nombre == M4T14S:
		cont = 1
	else:
		cont = 0
	
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Mantener jugadores con Nombre al refrescar')
else:
	pruebas_reprobadas.append('Mantener jugadores con Nombre al refrescar')
time.sleep(2)




#Agregar mas de 4 jugadores con nombre al azar
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("M4T14S",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("T0Ty",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("C4asdasd",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("1313",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("NoobMaster69",Keys.ENTER)
	time.sleep(0.5)

	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar mas de 4 jugadores con nombre al azar')
else:
	pruebas_reprobadas.append('Agregar mas de 4 jugadores con nombre al azar')
time.sleep(2)


#Agregar 2 jugadores con mismo nombre
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Lucas",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Lucas",Keys.ENTER)
	driver.find_element_by_xpath("//html/body/div/div/div[1]/form/div[2]")
	cont = 0;

except:
	cont = 1

if cont == 1:
	pruebas_aprobadas.append('Agregar 2 jugadores con mismo nombre')
else:
	pruebas_reprobadas.append('Agregar 2 jugadores con mismo nombre')
time.sleep(2)



#quitar jugador
driver.get("http://181.43.143.136:2000/piramide/")
try:
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("John",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/a").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('quitar jugador')
else:
	pruebas_reprobadas.append('quitar jugador')
time.sleep(2)


#iniciar juego sin jugadores
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('iniciar juego sin jugadores')
else:
	pruebas_reprobadas.append('iniciar juego sin jugadores')
time.sleep(2)



#iniciar juego con 1 jugador
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("John",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('iniciar juego con 1 jugador')
else:
	pruebas_reprobadas.append('iniciar juego con 1 jugador')
time.sleep(2)



#iniciar juego con 2 jugadores
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("John",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Melendez",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('iniciar juego con 2 jugadores')
else:
	pruebas_reprobadas.append('iniciar juego con 2 jugadores')
time.sleep(2)




#iniciar juego con 3 jugadores
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Odin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Loki",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Thor",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('iniciar juego con 3 jugadores')
else:
	pruebas_reprobadas.append('iniciar juego con 3 jugadores')
time.sleep(2)


#iniciar juego con 4 jugadores
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Odin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Loki",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Thor",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Kratos",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(1)
	driver.execute_script("document.body.style.zoom='25%'")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('iniciar juego con 4 jugadores')
else:
	pruebas_reprobadas.append('iniciar juego con 4 jugadores')
time.sleep(2)


#iniciar juego con mas de 4 jugadores
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Odin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Loki",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Thor",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Kratos",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Zeus",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(1)
	driver.execute_script("document.body.style.zoom='25%'")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('iniciar juego con mas de 4 jugadores')
else:
	pruebas_reprobadas.append('iniciar juego con mas de 4 jugadores')



#Ingresar 4 jugadores,quitar a uno e iniciar juego
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Odin",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Loki",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Thor",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Kratos",Keys.ENTER)
	time.sleep(0.5)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/a").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(0.5)
	driver.execute_script("document.body.style.zoom='25%'")

	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Ingresar 4 jugadores,quitar a uno e iniciar juego')
else:
	pruebas_reprobadas.append('Ingresar 4 jugadores,quitar a uno e iniciar juego')
time.sleep(2)



#Mostrar nombre de los jugadores al iniciar el juego
driver.get("http://181.43.143.136:2000/piramide/")
try:
	name1 = 'Odin'
	name2 = 'Loki'
	name3 = 'Thor'
	name4 = 'Kratos'
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys(name1,Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys(name2,Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys(name3,Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys(name4,Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)

	driver.execute_script("document.body.style.zoom='25%'")
	cont=1


	
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Mostrar nombre de los jugadores al iniciar el juego')
else:
	pruebas_reprobadas.append('Mostrar nombre de los jugadores al iniciar el juego')
time.sleep(2)




#mostrar mano jugadores
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Poseidon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Zeus",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Hades",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Cata",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	driver.find_element_by_xpath("/html/body/div/div/div[7]/ul")
	cont = 1
except:
	cont = 0
if cont == 1:
	pruebas_aprobadas.append('Mostrar mano jugadores')
else:
	pruebas_reprobadas.append('Mostrar mano jugadores')
time.sleep(2)




#Reiniciar juego al refrescar pagina
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Poseidon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Zeus",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Hades",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Cata",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(2)
	
	driver.refresh()
	time.sleep(1)
	driver.execute_script("document.body.style.zoom='25%'")
	driver.find_element_by_xpath("/html/body/div/div/h1")
	cont=1

except:
	cont = 0

if cont == 1:
	pruebas_aprobadas.append('Reiniciar juego al refrescar pagina')
else:
	pruebas_reprobadas.append('Reiniciar juego al refrescar pagina')
time.sleep(2)


#Mostrar titulo de juego
driver.get("http://181.43.143.136:2000/piramide/")

try:
	
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Poseidon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Zeus",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Hades",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Cata",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div/div/h1')
	cont=1
except:
	cont=0
if cont == 1:
	pruebas_aprobadas.append('Mostrar titulo de juego')
else:
	pruebas_reprobadas.append('Mostrar titulo de juego')
time.sleep(2)


#Titulo se mantiene al refrescar pagina
driver.get("http://181.43.143.136:2000/piramide/")

try:
	
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Poseidon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Zeus",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Hades",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Cata",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div/div/h1')
	time.sleep(1)
	driver.refresh()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div/div/h1')
	cont=1
except:
	cont=0
if cont == 1:
	pruebas_aprobadas.append('Titulo se mantiene al refrescar pagina')
else:
	pruebas_reprobadas.append('Titulo se mantiene al refrescar pagina')
time.sleep(2)





#Terminar turno jugador
driver.get("http://181.43.143.136:2000/piramide/")

try:
	
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Arthas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Uther",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Therenas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Varian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath('boton_terminar_turno')

except:
	cont=0
if cont == 1:
	pruebas_aprobadas.append('Terminar turno jugador')
else:
	pruebas_reprobadas.append('Terminar turno jugador')
time.sleep(2)


#Elegir tamano piramide
driver.get("http://181.43.143.136:2000/piramide/")

try:
	time.sleep(1)
	driver.find_element_by_xpath("ingrese_tamano_piramide").send_keys("8")
	cont=1
except:
	cont=0
if cont == 1:
	pruebas_aprobadas.append('Elegir tamano piramide')
else:
	pruebas_reprobadas.append('Elegir tamano piramide')
time.sleep(2)


#Modificar nombre de un jugador
driver.get("http://181.43.143.136:2000/piramide/")

try:
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Arthas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("boton_editar_nombre").click()
	driver.find_element_by_xpath("cuadro_texto").send_keys("Poseidon")
	cont=1
except:
	cont=0
if cont == 1:
	pruebas_aprobadas.append('Modificar nombre de un jugador')
else:
	pruebas_reprobadas.append('Modificar nombre de un jugador')
time.sleep(2)


#Terminar partida
driver.get("http://181.43.143.136:2000/piramide/")

try:
	
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Arthas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Uther",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Therenas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Varian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath('boton_terminar_partida')

except:
	cont=0
if cont == 1:
	pruebas_aprobadas.append('Terminar partida')
else:
	pruebas_reprobadas.append('Terminar partida')
time.sleep(2)


#Manos diferentes para cada jugador
driver.get("http://181.43.143.136:2000/piramide/")

try:
	
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Arthas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Uther",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Therenas",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Varian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)

	carta1=driver.find_element_by_xpath("/html/body/div/div/div[7]/ul/li[1]/ul[2]/li/img")
	carta2=driver.find_element_by_xpath("/html/body/div/div/div[7]/ul/li[2]/ul[2]/li/img")
	carta3=driver.find_element_by_xpath("/html/body/div/div/div[7]/ul/li[3]/ul[2]/li/img")
	carta4=driver.find_element_by_xpath("/html/body/div/div/div[7]/ul/li[4]/ul[2]/li/img")

	if carta1 != carta4 and carta1 != carta3 and carta1 != carta2:
		cont=1
	else:
		cont=0
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Manos diferentes para cada jugador')
else:
	pruebas_reprobadas.append('Manos diferentes para cada jugador')
time.sleep(2)



#Quitar jugador durante la partida
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 1")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Quitar jugador durante la partida')
else:
	pruebas_reprobadas.append('Quitar jugador durante la partida')
time.sleep(2)





#Quitar 2 jugador durante la partida
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 1")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 2")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Quitar 2 jugadores durante la partida')
else:
	pruebas_reprobadas.append('Quitar 2 jugadores durante la partida')
time.sleep(2)



#Quitar 3 jugadores durante la partida
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 1")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 2")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 3")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Quitar 3 jugadores durante la partida')
else:
	pruebas_reprobadas.append('Quitar 3 jugadores durante la partida')
time.sleep(2)




#Quitar 4 jugadores durante la partida
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 1")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 2")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 3")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 4")	

	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Quitar 4 jugadores durante la partida')
else:
	pruebas_reprobadas.append('Quitar 4 jugadores durante la partida')
time.sleep(2)




#Quitar mas de 4 jugadores durante la partida
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("DujovGamer",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 1")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 2")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 3")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 4")
	time.sleep(1)
	driver.find_element_by_xpath("Eliminar jugador 5")		

	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Quitar mas de 4 jugadores durante la partida')
else:
	pruebas_reprobadas.append('Quitar mas de 4 jugadores durante la partida')
time.sleep(2)


#permitir foto de pantalla
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("DujovGamer",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.save_screenshot("pantallazo_carrete.png")

	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('permitir foto de pantalla')
else:
	pruebas_reprobadas.append('permitir foto de pantalla')
time.sleep(2)


#Mostrar Piramide
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("DujovGamer",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Mostrar Piramide')
else:
	pruebas_reprobadas.append('Mostrar Piramide')
time.sleep(2)

#Agregar jugador con nombre en codigo ASCII
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("╚Ü¢Æ§  ¢¥ƒ",Keys.ENTER)
	time.sleep(1)
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con nombre en codigo ASCII')
else:
	pruebas_reprobadas.append('Agregar jugador con nombre en codigo ASCII')
time.sleep(2)


#Agregar jugador con nombre vacio
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div")
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con nombre vacio')
else:
	pruebas_reprobadas.append('Agregar jugador con nombre vacio')
time.sleep(2)



#Mostrar estadisticas
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mister Demian",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Rey Luciano",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("QA # BEA",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Swimer Martin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("DujovGamer",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	time.sleep(1)
	driver.find_element_by_xpath("Mostrar estadisticas")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Mostrar estadisticas')
else:
	pruebas_reprobadas.append('Mostrar estadisticas')
time.sleep(2)


#Mostrar menu
driver.get("http://181.43.143.136:2000/piramide/")
try:
	driver.find_element_by_xpath("Mostrar MENU")
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Visualizar menu')
else:
	pruebas_reprobadas.append('Visualizar menu')
time.sleep(2)



#Agregar jugador con nombre usando solo espacio
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys(" ",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div")
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con nombre usando solo espacio')
else:
	pruebas_reprobadas.append('Agregar jugador con nombre usando solo espacio')
time.sleep(2)



#Agregar jugador con nombre alfanumerico y codigo ASCII
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("╚Ü¢Æ§  ¢¥ƒ 13a14 ácéntós",Keys.ENTER)
	time.sleep(1)
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con nombre alfanumerico y codigo ASCII')
else:
	pruebas_reprobadas.append('Agregar jugador con nombre alfanumerico y codigo ASCII')
time.sleep(2)



#Agregar jugador con alfabeto en idioma chino
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("你好你好吗",Keys.ENTER)
	time.sleep(1)
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con alfabeto en idioma chino')
else:
	pruebas_reprobadas.append('Agregar jugador con alfabeto en idioma chino')
time.sleep(2)



#Agregar jugador con alfabeto en idioma arabe
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("سلام. چطوری",Keys.ENTER)
	time.sleep(1)
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con alfabeto en idioma arabe')
else:
	pruebas_reprobadas.append('Agregar jugador con alfabeto en idioma arabe')
time.sleep(2)




#Agregar jugador con alfabeto en idioma ruso
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Привет, как дела",Keys.ENTER)
	time.sleep(1)
	cont = 1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Agregar jugador con alfabeto en idioma ruso')
else:
	pruebas_reprobadas.append('Agregar jugador con alfabeto en idioma ruso')
time.sleep(2)


#Ajustar tamano de pagina
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mono",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Leon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Perro",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gato",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Ajustar tamano de pagina')
else:
	pruebas_reprobadas.append('Ajustar tamano de pagina')
time.sleep(2)


#Iniciar juego con 5 jugadores
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mono",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Leon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Perro",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gato",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Delfin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='25%'")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Iniciar juego con 5 jugadores')
else:
	pruebas_reprobadas.append('Iniciar juego con 5 jugadores')
time.sleep(2)



#Iniciar juego con 6 jugadores
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mono",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Leon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Perro",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gato",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Delfin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gorila",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='22%'")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Iniciar juego con 6 jugadores')
else:
	pruebas_reprobadas.append('Iniciar juego con 6 jugadores')
time.sleep(2)


#Iniciar juego con 7 jugadores
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mono",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Leon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Perro",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gato",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Delfin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gorila",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Caballo",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='20%'")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Iniciar juego con 7 jugadores')
else:
	pruebas_reprobadas.append('Iniciar juego con 7 jugadores')
time.sleep(2)



#Iniciar juego con 8 jugadores
driver.get("http://181.43.143.136:2000/piramide/")

try:
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Mono",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Leon",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Perro",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gato",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Delfin",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Gorila",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Caballo",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='id_name']").send_keys("Aguila",Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div[2]/a").click()
	time.sleep(2)
	driver.execute_script("document.body.style.zoom='20%'")
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/div/div.")
	cont=1
except:
	cont=0

if cont == 1:
	pruebas_aprobadas.append('Iniciar juego con 8 jugadores')
else:
	pruebas_reprobadas.append('Iniciar juego con 8 jugadores')
time.sleep(2)

#resultado final
driver.close()
print("pruebas_aprobadas: ")
for i in pruebas_aprobadas:
	print(i)
print(" ")
print("pruebas_reprobadas: ")
for j in pruebas_reprobadas:
	print(j)