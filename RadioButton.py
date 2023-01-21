import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazisi = QLabel("Hangi Dili Yazabiliyorsun")

        self.python = QRadioButton("python")
        self.java = QRadioButton("Java")
        self.C = QRadioButton("C#")

        self.yazi_alani = QLabel("")
        self.button = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.C)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.button.clicked.connect(lambda : self.TikliMi(self.python.isChecked(),self.java.isChecked(),self.C.isChecked(),self.yazi_alani))
        self.setWindowTitle("RadioButton ")

        self.show()

    def TikliMi(self, python,java,C,yazi_alani):
        yazi = ""
        if python:
            yazi += "Python "
        if java :
            yazi += "java "
        if C:
            yazi += "C "

        yazi_alani.setText(yazi)
app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())