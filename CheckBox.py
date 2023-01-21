

import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Python Yazıyor Musun ? ")
        self.yazi_alani = QLabel("")
        self.button = QPushButton("Tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("CheckBox")
        self.button.clicked.connect(lambda  : self.TiklandiMi(self.checkbox.isChecked(),self.yazi_alani))
        self.show()

    def TiklandiMi(self,checkbox,yazi_alani) :
        if checkbox :
            yazi_alani.setText("CheckBox işaretli")
        else :
            yazi_alani.setText("Yazi Alanı işaretli değil")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
