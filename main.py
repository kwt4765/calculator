import sys # 빌트 인 모듈로, 시스템 명령어를 수행할 수 있도록 도와준다.
from PyQt5.QtWidgets import QApplication, QWidget

#Qwidget을 기반으로 한 클래스를 설계하여 추후 객체 생성하도록 하겠다!
class Calculator(QWidget) : 

    #super() : 클래스가 어떤 객체를 기반으로 만들어 질 때, 그 기반 객체를 뜻한다.
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show()

#이 파일을 직접 실행할 시에만 명령을 수행하겠다!    
if __name__=='__main__' :
    app = QApplication(sys.argv) # 시스템에서 주어지는 인수를 받아 앱을 켜겠다.
    view = Calculator() # 위에서 만든 칼큘레이터 객체를 생성하겠다.
    sys.exit(app.exec_()) # 창이 꺼질 때 시스템도 끄겠다.

