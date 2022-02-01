import sys
import var
import events
import clients
from ventana import *
from windowAviso import *



class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.Salir.clicked.connect(events.Eventos.Salir)
        var.sexo=(var.ui.radioButtonFem, var.ui.radioButtonMas)
        #for i in var.sexo:
           # i.toggled.connect(clients.Clientes.selSexo)
        '''
        Eventos cada de texto
        '''
        var.ui.CampoDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.Aceptar.clicked.connect(clients.Clientes.validarDNI)
        var.ui.grupoSexo.buttonClicked.connect(clients.Clientes.selSexo)

        var.checkPago = (var.ui.checkEfect, var.ui.checkTransfe, var.ui.checkTarjeta)
        for i in var.checkPago:
            i.stateChanged.connect(events.Eventos.grupoPago)

        clients.Clientes.cargarProv()
        var.ui.comboBox.activated[str].connect(clients.Clientes.selProv)

        #var.ui.comboBox.editingFinished.connect(clients.Clientes.selProv)

class avisoSalir(QtWidgets.QDialog):
    def __init__(self):
        super(avisoSalir, self).__init__()
        var.avisoSalir = Ui_Form()
        var.avisoSalir.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.avisoSalir = avisoSalir()
    window.show()
    sys.exit(app.exec())