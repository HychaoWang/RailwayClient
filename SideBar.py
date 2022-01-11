from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
from qt_material import apply_stylesheet
from ModelCombo import *


class SideBar(QWidget):

    def __init__(self):
        super(SideBar, self).__init__()
        self.ini()

    def ini(self):
        self.side_layout = QVBoxLayout()
        self.run_bt = QPushButton('启动')
        self.status_bt = QPushButton("状态")
        self.graph_bt = QPushButton("图像")
        self.data_bt = QPushButton("数据")
        self.stop_bt = QPushButton('关闭')
        self.other_bt = QPushButton('其他')
        self.model_cb = ModelCombo()
        self.bt_list = [self.run_bt, self.status_bt, self.graph_bt, self.data_bt, self.stop_bt,self.other_bt]
        for bt in self.bt_list:
            self.side_layout.addWidget(bt)
            bt.setStyleSheet('color:white;font-size:15px;background:rgb(27,28,64)')
            bt.setFixedSize(70, 70)
        self.side_layout.addWidget(self.model_cb)
        self.model_cb.setFixedSize(70, 40)
        self.side_layout.setSpacing(20)
        self.side_layout.setAlignment(Qt.AlignTop)
        self.side_layout.setContentsMargins(15, 20, 15, 40)
        self.setLayout(self.side_layout)
        # self.setStyleSheet("background:black")

    def choose_run_status(self):
        for bt in self.bt_list:
            bt.setStyleSheet("background-color:(39,44,49); color:cyan;")
        self.status_bt.setStyleSheet("background-color:cyan; color:#1d1c1d;");

    def choose_graph(self):
        for bt in self.bt_list:
            bt.setStyleSheet("background-color:(39,44,49); color:cyan;")
        self.graph_bt.setStyleSheet("background-color:cyan; color:#1d1c1d;");

    def choose_data(self):
        for bt in self.bt_list:
            bt.setStyleSheet("background-color:(39,44,49); color:cyan;")
        self.data_bt.setStyleSheet("background-color:cyan; color:#1d1c1d;");


if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = SideBar()
        apply_stylesheet(app, theme='dark_teal.xml')
        # main.showFullScreen()
        main.show()
        sys.exit(app.exec_())