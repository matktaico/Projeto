from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit, QLabel, QTableWidget
from PyQt5 import uic, QtWidgets
import sys
import mysql.connector 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#conexao com o bd
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'ensino'
)
#conexao com o servidor de emails
host = 'smtp.gmail.com'
port = 587
user = 'bezerraomatheus@gmail.com'
password = open('senha.txt').read().strip()
server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(user, password)

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("C:\\Users\\Steph\\Desktop\\projeto python\\plataforma.ui", self)

#Cadastro de users:

        self.lineEdit_escola = self.findChild(QLineEdit, "lineEdit_1")
        self.lineEdit_mail1 = self.findChild(QLineEdit, "lineEdit_2")
        self.lineEdit_mail2 = self.findChild(QLineEdit, "lineEdit_3")
        self.lineEdit_senha1 = self.findChild(QLineEdit, "lineEdit_4")
        self.lineEdit_senha2 = self.findChild(QLineEdit, "lineEdit_5")
        self.label_mensagem = self.findChild(QLabel, "label")
        self.label_mensagem_login = self.findChild(QLabel, "label_2")
        self.pushbutton = self.findChild(QPushButton, "Button_cadastrar")
        self.pushbutton.clicked.connect(self.cadastrar)
#Chamando Login

        self.nome_login = self.findChild(QLineEdit, "lineEdit_6")
        self.senha_login = self.findChild(QLineEdit, "lineEdit_7")
        self.botao_login = self.findChild(QPushButton,"Button_entrar")
        self.botao_login.clicked.connect(self.login)
        
#Cadastro de alunos


        self.show()

    def cadastrar(self):
        lineEdit_escola = self.lineEdit_escola.text()
        lineEdit_mail1= self.lineEdit_mail1.text()
        lineEdit_mail2 = self.lineEdit_mail2.text()
        lineEdit_senha1 = self.lineEdit_senha1.text()
        lineEdit_senha2 = self.lineEdit_senha2.text()

#Cadastro no BD
        if lineEdit_senha1 == lineEdit_senha2 and lineEdit_mail1 == lineEdit_mail2:
            try:
                
                cursor= conexao.cursor()
                comando_SQL = "INSERT INTO cadastro (escola,email,email2,senha,senha2) VALUES (%s,%s,%s,%s,%s)"
                dados = (str(lineEdit_escola),str(lineEdit_mail1),str(lineEdit_mail2),str(lineEdit_senha1),str(lineEdit_senha2) )
                cursor.execute(comando_SQL,dados)
                conexao.commit()
                #conexao.close
                

                # Criando mensagem
                message = self.lineEdit_escola.text()
                print('Criando mensagem...')
                email_msg = MIMEMultipart()
                email_msg['From'] = user
                email_msg['To'] = 'msb2@discente.ifpe.edu.br'
                email_msg['Subject'] = 'Ensino'
                print('Adicionando texto...')
                email_msg.attach(MIMEText(message, 'plain'))

                # Enviando mensagem
                print('Enviando mensagem...')
                server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
                print('Mensagem enviada!')
                server.quit()

                self.label_mensagem.setText("Cadastrado com sucesso, email enviado!")
            except mysql.connector.Error as err:
                print("erro ao inserir os dados: ", err)
        else:
            self.label_mensagem.setText("Senhas ou emails diferentes!")

 

    def login(self):
        global window_2
        self.hide()
        window_2.show()
        login = self.nome_login.text()
        senha = self.senha_login.text()
        if login == self.lineEdit_senha1 and senha == self.lineEdit_mail1:
            try:
                cursor= conexao.cursor()
                comando_SQL = "SELECT * FROM cadastro"
                cursor.execute(comando_SQL)
                dados_lidos = cursor.fetchall()
    

                self.hide()
                window_2.show
                
    
                #conexao.close
                self.label_mensagem_login.setText("logado com sucesso!")
            except mysql.connector.Error as err:
                print("erro ao inserir os dados: ", err)
        else:
            self.label_mensagem_login.setText("Senhas ou emails diferentes!")

        
       
        #janela = UI_menu_iniciar()
class UI_menu_iniciar(QMainWindow):
    def __init__(self):
        super(UI_menu_iniciar, self).__init__()
        uic.loadUi("C:\\Users\\Steph\\Desktop\\projeto python\\menu_iniciar.ui", self)       

    


#Carregando widgets da página de cadastro do aluno

        self.botao_cadastro = self.findChild(QPushButton, "pushButton")
        self.botao_consulta = self.findChild(QPushButton, "pushButton_2")
        self.botao_boletim = self.findChild(QPushButton, "pushButton_4")
        self.botao_cadastro.clicked.connect(self.alunos)
        self.botao_consulta.clicked.connect(self.consulta)
        self.botao_boletim.clicked.connect(self.boletim)
        

    def alunos(self):
        global window_3
        window_3.show()
         

    def consulta(self):
        global window_4
        window_4.show()

    def boletim(self):
        global window_5
        window_5.show()



            
class UI_cadastro(QMainWindow):
    def __init__(self):
        super(UI_cadastro, self).__init__()
        uic.loadUi("C:\\Users\\Steph\\Desktop\\projeto python\\menu_cadastro.ui", self)

        self.nome_aluno = self.findChild(QLineEdit, "nome_aluno")
        self.pai_aluno = self.findChild(QLineEdit, "pai_aluno")
        self.mae_aluno = self.findChild(QLineEdit, "mae_aluno")
        self.nascimento_aluno = self.findChild(QLineEdit, "nascimento_aluno")
        self.serie = self.findChild(QLineEdit,"serie_aluno")
        self.turma = self.findChild(QLineEdit, "turma_aluno")
        self.mensagem = self.findChild(QLabel,"label_9")
        self.cadastro_aluno = self.findChild(QPushButton, "cadastro_aluno")
        self.cadastro_aluno.clicked.connect(self.cadastrar)

    def cadastrar(self):
        nome_aluno = self.nome_aluno.text()
        pai_aluno = self.pai_aluno.text()
        mae_aluno = self.mae_aluno.text()
        nascimento = self.nascimento_aluno.text()
        serie = self.serie.text()
        turma = self.turma.text()

        cursor= conexao.cursor()
        comando_SQL = "INSERT INTO alunos (nome,pai,mae,nascimento,serie,turma) VALUES (%s,%s,%s,%s,%s,%s)"
        dados = (str(nome_aluno),str(pai_aluno),str(mae_aluno),str(nascimento),str(serie),str(turma) )
        cursor.execute(comando_SQL,dados)
        conexao.commit()
        self.mensagem.setText("Aluno cadastrado com sucesso!")
         

    

class UI_consulta(QMainWindow):
    def __init__(self):
        super(UI_consulta, self).__init__()
        uic.loadUi("C:\\Users\\Steph\\Desktop\\projeto python\\consulta_dados.ui", self)

        self.consulta_aluno = self.findChild(QLineEdit, "lineEdit")
        self.nasc_aluno = self.findChild(QLineEdit, "lineEdit_2")
        self.botao_enviar = self.findChild(QPushButton, "pushButton")
        self.botao_enviar.clicked.connect(self.consultar_dados)

    def consultar_dados(self):
        cursor = conexao.cursor()
        comando_SQL = "SELECT * FROM alunos"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        window_4.tableWidget.setRowCount(len(dados_lidos))
        window_4.tableWidget.setColumnCount(7)

        for i in range(0, len(dados_lidos)):
            for j in range(0,7):
                window_4.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


class UI_boletim(QMainWindow):
    def __init__(self):
        super(UI_boletim, self).__init__()
        uic.loadUi("C:\\Users\\Steph\\Desktop\\projeto python\\menu_boletim.ui", self)

        self.aluno_nome = self.findChild(QLineEdit, "lineEdit")
        self.aluno_serie = self.findChild(QLineEdit, "lineEdit_2")
        self.aluno_turma = self.findChild(QLineEdit, "lineEdit_3")
        self.aluno_nota1 = self.findChild(QLineEdit, "lineEdit_4")
        self.aluno_nota2 = self.findChild(QLineEdit, "lineEdit_5")
        self.aluno_nota3 = self.findChild(QLineEdit, "lineEdit_6")
        self.enviar_botao = self.findChild(QPushButton, "pushButton")
        self.mostrar_nota = self.findChild(QPushButton, "pushButton_2")
        self.enviar_botao.clicked.connect(self.inserir_nota)
        self.mostrar_nota.clicked.connect(self.mostrar)
        

    def inserir_nota(self):
        aluno_nome = self.aluno_nome.text()
        aluno_serie = self.aluno_serie.text()
        aluno_turma = self.aluno_turma.text()
        aluno_nota1 = self.aluno_nota1.text()
        aluno_nota2 = self.aluno_nota2.text()
        aluno_nota3 = self.aluno_nota3.text()

        cursor = conexao.cursor()
        notas = "INSERT INTO notas(nome, serie, turma, nota1, nota2, nota3) VALUES(%s,%s,%s,%s,%s,%s)"
        salvar = (str(aluno_nome), str(aluno_serie), str(aluno_turma), str(aluno_nota1), str(aluno_nota2), str(aluno_nota3))
        cursor.execute(notas, salvar)
        conexao.commit()

    def mostrar(self):
        cursor = conexao.cursor()
        comando_SQL = "SELECT * FROM notas"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        window_5.tableWidget.setRowCount(len(dados_lidos))
        window_5.tableWidget.setColumnCount(8)

        for i in range(0, len(dados_lidos)):
            for j in range(0,8):
                window_5.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

            
    

app = QApplication(sys.argv)
window = UI()
window_2 = UI_menu_iniciar()
window_3 = UI_cadastro()
window_4 = UI_consulta()
window_5 = UI_boletim()
app.exec_()