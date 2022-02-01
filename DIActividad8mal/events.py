import sys
import var

class Eventos:

    def Salir(self):
        try:
            var.avisoSalir.show()
            if var.avisoSalir.exec():
                sys.exit()
            else:
                var.avisoSalir.hide()
        except Exception as error:
            print("Error %s:" % str(error))

    def grupoPago(self):
        try:
            if var.ui.checkEfect.isChecked():
                print('Pago en efectivo')
            if var.ui.checkTarjeta.isChecked():
                print('Pago con tarjeta')
            if var.ui.checkTransfe.isChecked():
                print('Pago con transferencia')
        except Exception as error:
            print('Error: %s ' % str(error))

