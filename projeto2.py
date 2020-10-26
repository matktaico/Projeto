from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit
from PyQt5 import uic, QtWidgets
import sys
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ensino"
)
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\projeto\\plataforma.ui", self)
        
        self.lineEdit_escola = self.findChild(QLineEdit, "lineEdit_1")
        self.lineEdit_mail1 = self.findChild(QLineEdit, "lineEdit_2")
        self.lineEdit_mail2 = self.findChild(QLineEdit, "lineEdit_3")
        self.lineEdit_senha1 = self.findChild(QLineEdit, "lineEdit_4")
        self.lineEdit_senha2 = self.findChild(QLineEdit, "lineEdit_5")
        self.pushbutton = self.findChild(QPushButton, "Button_cadastrar")
        self.pushbutton.clicked.connect(self.cadastrar)

        self.show()

    def cadastrar(self):
        cursor = conexao.cursor()
        cadastro = "INSERT INTO escolas(nome, email, email2, senha, senha2) VALUES(%s,%s,%s,%d,%d)"
        preencher = (str(self.lineEdit_escola), str(self.lineEdit_mail1), str(self.lineEdit_mail2), str(self.lineEdit_senha1), str(self.lineEdit_senha2))
        cursor.execute(cadastro,preencher)
        conexao.commit()
        print(cursor.rowcount, "Cadastrado com sucesso")
        
app = QApplication(sys.argv)
window = UI()
app.exec_()

