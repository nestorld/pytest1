from bottle import route, run
import socket


@route('/dockertest')
def dockertest():
	hostname = socket.gethostname()
	respuesta = "<p align=\"center\">Container Docker Python funcionando con otro cambio</p> <p align=\"center\">Hostname = {0}</p>".format(hostname)
	return respuesta


run(host='0.0.0.0', port=8200)
