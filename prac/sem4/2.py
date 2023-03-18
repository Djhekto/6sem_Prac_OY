import PyQt6#pylance
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
#
layout = QVBoxLayout()

txt1 = QLineEdit(";kfmasknf")
txt2 = QLineEdit("nf")
layout.addWidget(txt1)
layout.addWidget(txt2)

button1 = QPushButton("push me")
def ff1():
    button1.setText("and then just touch me")

button1.clicked.connect(ff1)
layout.addWidget(button1)

window.setLayout(layout)
#
window.show()
app.exec()



