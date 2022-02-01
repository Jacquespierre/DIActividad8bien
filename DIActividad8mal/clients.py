import var


class Clientes():
    def validarDNI():
        try:
            dni = var.ui.CampoDNI.text()
            var.ui.CampoDNI.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # letras dni
            dig_ext = 'XYZ'  # digito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()  # conver la letra mayusculas
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.label.setStyleSheet('QLabel {color: green;}')
                    var.ui.label.setText('V')
                else:
                    var.ui.label.setStyleSheet('QLabel {color: red;}')
                    var.ui.label.setText('X')
            else:
                var.ui.label.setStyleSheet('QLabel {color: red;}')
                var.ui.label.setText('X')
        except Exception as error:
            print('Error en modulo validar DNI', error)

    def selSexo():
        try:
            if var.ui.radioButtonFem.isChecked():
                print('Marcado femenino')
            if var.ui.radioButtonMas.isChecked():
                print('Marcado masculino')
        except Exception as error:
            print('Error en módulo seccionar sexo:', error)

    def cargarProv():
        try:
            prov = [' ', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.comboBox.addItem(i)
        except  Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ', prov)
            return prov
        except Exception as error:
            print('Error: %s ' % str(error))

