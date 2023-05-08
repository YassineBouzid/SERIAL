from PyQt5 import QtCore, QtGui, QtWidgets
import serial 

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)
class Ui_Serial_commande(object):
    def setupUi(self, Serial_commande):
        Serial_commande.setObjectName("Serial_commande")
        Serial_commande.resize(300, 120)
        self.centralwidget = QtWidgets.QWidget(Serial_commande)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("com4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setText("HV : 1 {CR}")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1)
        self.RunButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.serial_run())
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.RunButton.setFont(font)
        self.RunButton.setObjectName("RunButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.RunButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        Serial_commande.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Serial_commande)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 21))
        self.menubar.setObjectName("menubar")
        Serial_commande.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Serial_commande)
        self.statusbar.setObjectName("statusbar")
        Serial_commande.setStatusBar(self.statusbar)

        self.retranslateUi(Serial_commande)
        QtCore.QMetaObject.connectSlotsByName(Serial_commande)

    def retranslateUi(self, Serial_commande):
        _translate = QtCore.QCoreApplication.translate
        Serial_commande.setWindowTitle(_translate("Serial_commande", "Serial"))
        self.label.setText(_translate("Serial_commande", "Com Port:"))
        self.label_2.setText(_translate("Serial_commande", "Command:"))
        self.RunButton.setText(_translate("Serial_commande", "Run"))

    def serial_run(self):
        ardport = self.lineEdit_2.text()
        command = self.lineEdit_1.text()
        print("ardport==",ardport,'command===',command,"bcommand======",bytearray(command,'utf8'))
        arddata = serial.Serial(ardport,9600)
        
        arddata.write(bytes(command ,'utf8'))

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Serial_commande = QtWidgets.QMainWindow()
    ui = Ui_Serial_commande()
    ui.setupUi(Serial_commande)
    Serial_commande.show()
    sys.exit(app.exec_())
