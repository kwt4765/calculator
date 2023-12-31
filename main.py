import sys # 빌트 인 모듈로, 시스템 명령어를 수행할 수 있도록 도와준다.
from PyQt5.QtWidgets import (QApplication,
                            QWidget, QPushButton, QVBoxLayout, 
                            QMessageBox, QPlainTextEdit, QHBoxLayout) 

import random # 내 맘대로 로또 추첨 기능 추가할래

from PyQt5.QtGui import QIcon
#Qwidget을 기반으로 한 클래스를 설계하여 추후 객체 생성하도록 하겠다!

from prompt import sayHello


class Calculator(QWidget) : 

    #super() : 클래스가 어떤 객체를 기반으로 만들어 질 때, 그 기반 객체를 뜻한다.
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)
        
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self) :
        lottoNum = random.sample(range(1, 46), 6)
        self.te1.appendPlainText(str(lottoNum))
    
    def clearMessage(self) :
        self.te1.clear()

#이 파일을 직접 실행할 시에만 명령을 수행하겠다!    
if __name__=='__main__' :
    sayHello()
    app = QApplication(sys.argv) # 시스템에서 주어지는 인수를 받아 앱을 켜겠다.
    view = Calculator() # 위에서 만든 칼큘레이터 객체를 생성하겠다.
    sys.exit(app.exec_()) # 창이 꺼질 때 시스템도 끄겠다.

