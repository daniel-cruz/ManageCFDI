#pip install appjar
#
#pip install PyGTK

from appJar import gui
import functions

def press(button):
    if button == "Cancelar":
        app.stop()
    else:
        source = app.getEntry("source")
        destination = app.getEntry("destination")
        errors = functions.sortCFDI(source, destination)
        if not len(errors):
        	app.infoBox("Operacion exitosa", "Se ordenaron los CFDIs exitosamente")
        else:
        	texto = ""
        	for filename in errors:
        		texto += filename + " : " + errors[filename]
        	app.errorBox("Operacion con errores", texto)

app = gui()

app.startTabbedFrame("TabbedFrame")
app.startTab("Ordenar CFDIs")
app.addLabel("source", "Origen")
app.addDirectoryEntry("source")
app.addLabel("destination", "Destino")
app.addDirectoryEntry("destination")
app.addButtons(["Ordenar", "Cancelar"], press)
app.stopTab()

app.startTab("Descargar CFDIs")

app.stopTab()

app.stopTabbedFrame()

app.go()