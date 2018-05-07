from bottle import route, run
import socket
import io
from os import path, mkdir, getcwd


@route('/persistent_test/<valor>', method='GET')
def persistent_test(valor):
	hostname = socket.gethostname()
	wd = "<p align=\"center\">Working Directory = {0}</p>".format(getcwd())
	respuesta = "<p align=\"center\">Contenedor de Docker Python funcionando</p> <p align=\"center\">Hostname = {0}</p> <p align=\"center\">Valor recibido = {1}</p>".format(hostname, valor)
	respuesta = respuesta + wd
	with io.open("./data/dataDocker.dat","w",encoding="utf8") as archivo:
		archivo.write(valor + "\n")

	return respuesta



#Si no existe, crea una carpeta data para almacenar la data persistente
datafolder = "data"
if path.exists(datafolder):
	if not(path.isdir(datafolder)):
		mkdir(datafolder)
else:
	mkdir(datafolder)

run(host='0.0.0.0', port=8300)
