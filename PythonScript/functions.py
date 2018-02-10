def sortCFDI(source, destination):
	import os
	import glob
	import shutil
	import time
	import datetime
	import sys
	from xml.dom import minidom

	source.strip()
	destination.strip()
	source += "/"
	destination += "/"
	errors = {}

	log  = open(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H_%M_%S') + ".csv", "w") 
	#log.write("sep=,")
	log.write("Estatus,Origen,Destino\n")
	for filename in glob.glob(source + '*.xml'):
		rfc = ""
	 	cfdi = minidom.parse(filename)
	 	for comprobante in cfdi.getElementsByTagName('cfdi:Comprobante'):
	 		if comprobante.attributes.has_key("fecha"):
	 			fecha = comprobante.attributes['fecha'].value.split('-')
	 		else:
	 			if comprobante.attributes.has_key("Fecha"):
	 				fecha = comprobante.attributes['Fecha'].value.split('-')
	 			else:
	 				fecha = None
	 	for receptor in cfdi.getElementsByTagName('cfdi:Emisor'):
	 		if receptor.attributes.has_key("rfc"):
	 			rfc = receptor.attributes['rfc'].value
	 		else:
	 			if receptor.attributes.has_key("Rfc"):
	 				rfc = receptor.attributes['Rfc'].value
	 			else:
	 				print "Error en:" + filename
			if not os.path.isdir(destination + rfc):
	 			os.mkdir(destination + rfc)
	 		if not os.path.isdir(destination + rfc + '/' + fecha[0]):
	 			os.mkdir(destination + rfc + '/' + fecha[0])
	 		if not os.path.isdir(destination + rfc + '/' + fecha[0] + '/' + fecha[1]):
	 			os.mkdir(destination + rfc + '/' + fecha[0] + '/' + fecha[1])
	 	try:
	 		shutil.copy(filename, destination + rfc + '/' + fecha[0] + '/' + fecha[1])
	 		log.write("Success," + filename + "," + destination + rfc + '/' + fecha[0] + '/' + fecha[1] + "\n")
	 	except IOError as e:
	 		log.write("Error," + filename + "," + "I/O error({0}): {1}".format(e.errno, e.strerror) + "\n")
	 		errors[filename] = "I/O error({0}): {1}".format(e.errno, e.strerror)
	 	except:
	 		log.write("Error," + filename + "," + str(sys.exc_info()[0]) + "\n")
	 		errors[filename] = str(sys.exc_info()[0])
	log.close()
	return errors