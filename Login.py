from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import util
from util import *
from PyQt5.QtCore import Qt
import sys
from qt_material import apply_stylesheet
from MainWindow import *
from util import *


class Login(QWidget):
    url = ""
    windowlist = []

    def __init__(self) -> None:
        super().__init__()
        self.ini()

    def ini(self):
        # size, center, title
        # self.resize(640, 300)
        self.center()
        self.setWindowTitle('Center')

        # Login button
        bt = QPushButton('登录')

        bt.setStyleSheet("QPushButton{color:white}"
                         "QPushButton:hover{color:white}"
                         "QPushButton{background-color:rgb((35,39,68)}"
                         "QPushButton{border:2px}"
                         "QPushButton{border-radius:10px}")
        # banner
        title = QLabel('用户登录')
        title.setFont(QFont("Times New Roman"))

        # label and textbox
        url_label = QLabel('URL:')
        url_label.setFont(QFont("Times New Roman", 16, QFont.Bold))
        url_label.setAlignment(Qt.AlignCenter)
        port_label = QLabel('Port:')
        port_label.setFont(QFont("Times New Roman", 16, QFont.Bold))
        port_label.setAlignment(Qt.AlignCenter)
        id_label = QLabel('ID:')
        id_label.setFont(QFont("Times New Roman", 16, QFont.Bold))
        id_label.setAlignment(Qt.AlignCenter)
        pw_label = QLabel('Password:')
        pw_label.setFont(QFont("Times New Roman", 16, QFont.Bold))
        pw_label.setAlignment(Qt.AlignCenter)
        url_label.setStyleSheet("color:white")
        port_label.setStyleSheet("color:white")
        id_label.setStyleSheet("color:white")
        pw_label.setStyleSheet("color:white")

        self.url_line = QLineEdit()
        self.port_line = QLineEdit()
        self.id_line = QLineEdit()
        self.pw_line = QLineEdit()
        self.url_line.setStyleSheet("color:white")
        self.port_line.setStyleSheet("color:white")
        self.id_line.setStyleSheet("color:white")
        self.pw_line.setStyleSheet("color:white")

        title.setStyleSheet("color:white;"
                            "font-size:30px;"
                            "font-weight:600")
        # qle1.textChanged[str].connect(self.onChanged)
        # qle2.textChanged[str].connect(self.onChanged)

        url_hlayout = QHBoxLayout()
        url_hlayout.addWidget(url_label, 1)
        url_hlayout.addWidget(self.url_line, 3)
        url_hlayout.addWidget(port_label, 1)
        url_hlayout.addWidget(self.port_line, 1)
        url_hwg = QWidget()
        url_hwg.setLayout(url_hlayout)

        id_hlayout = QHBoxLayout()
        id_hlayout.addWidget(id_label, 1)
        id_hlayout.addWidget(self.id_line, 5)
        id_hwg = QWidget()
        id_hwg.setLayout(id_hlayout)

        pw_hlayout = QHBoxLayout()
        pw_hlayout.addWidget(pw_label, 1)
        pw_hlayout.addWidget(self.pw_line, 5)
        pw_hwg = QWidget()
        pw_hwg.setLayout(pw_hlayout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addWidget(url_hwg)
        main_layout.addWidget(id_hwg)
        main_layout.addWidget(pw_hwg)
        main_layout.addWidget(bt)

        self.setLayout(main_layout)
        main_layout.setSpacing(30)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_part = QWidget()
        main_part.setLayout(main_layout)
        main_part.setObjectName("all")
        self.setStyleSheet("QWidget#all{border:3px solid white;} "
                           "QWidget#all{border-radius:15px;}"
                           "QWidget{background-color:rgb(35,39,68)}")

        all_layout = QHBoxLayout()
        # all_layout.setContentsMargins(560, 300, 560, 300)
        all_layout.addWidget(main_part)
        self.setLayout(all_layout)
        bt.clicked.connect(self.on_push_button_2_clicked)

        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):

        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_clicked(self):
        idtext = self.qle1.text()
        pwtext = self.qle2.text()
        print(idtext, pwtext)

    def on_push_button_2_clicked(self):  # 登录
        login_user = self.id_line.text()
        login_password = self.pw_line.text()
        self.url = util.url_check(self.url_line.text()) + ':' + self.port_line.text()
        print(self.url)

        if login_user == "" or login_password == "" or login_user == '用户名' or login_password == '密码':
            QMessageBox.warning(self, "提示", "用户名或密码不能为空！", QMessageBox.Yes)
            return

        if connect(self.url) == 200:
            if login(self.url, login_user, login_password) == 200:
                self.main_window = MainWindow()
                self.main_window.set_url(self.url)
                self.main_window.set_user(login_user)
                self.main_window.show()
                self.close()
            else:
                QMessageBox.warning(self, "提示", "用户名或密码错误", QMessageBox.Yes)
                return
        else:
            QMessageBox.warning(self, "提示", "连接服务器失败", QMessageBox.Yes)
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Login()
    w.show()
    sys.exit(app.exec_())
