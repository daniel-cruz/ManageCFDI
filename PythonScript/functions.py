def sortCFDI(source, destination):
	import os
	import glob
	import shutil
	from xml.dom import minidom
	source.strip()
	destination.strip()
	source += "/"
	destination += "/"
	errors = {}
	for filename in glob.glob(source + '*.xml'):
		rfc = ""
	 	cfdi = minidom.parse(filename)
	 	for comprobante in cfdi.getElementsByTagName('cfdi:Comprobante'):
	 		if comprobante.attributes.has_key("fecha"):
	 			fecha = comprobante.attributes['fecha'].value.split('-')
	 	for receptor in cfdi.getElementsByTagName('cfdi:Emisor'):
	 		if receptor.attributes.has_key("rfc"):
	 			rfc = receptor.attributes['rfc'].value
	 		else:
	 			if receptor.attributes.has_key("Rfc"):
	 				rfc = receptor.attributes['Rfc'].value
	 			else:
	 				print "Error en:" + filename
	 		if not os.path.isdir(destination + fecha[0]):
	 			os.mkdir(destination + fecha[0])
	 		if not os.path.isdir(destination + fecha[0] + '/' + fecha[1]):
	 			os.mkdir(destination + fecha[0] + '/' + fecha[1])
	 		if not os.path.isdir(destination + fecha[0] + '/' + fecha[1] + '/' + rfc):
	 			os.mkdir(destination + fecha[0] + '/' + fecha[1] + '/' + rfc)
	 	try:
	 		shutil.copy(filename, destination + fecha[0] + '/' + fecha[1] + '/' + rfc)
	 	except:
	 		errors[filename] = sys.exc_info()[0]
	return errors