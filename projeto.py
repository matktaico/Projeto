from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit
from PyQt5 import uic, QtWidgets
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("plataforma.ui", self)
        
        self.lineedit_1 = self.findChild(QLineEdit, "lineEdit_1")
        self.button = self.findChild(QPushButton, "Button_cadastrar")
        self.button.clicked.connect(self.clickedBtn) 
        
        
        self.show()
    
    def clickedBtn(self):
        self.lineedit_1.setPlainText("teste")
    
    
app = QApplication(sys.argv)
window = UI()
app.exec_()

