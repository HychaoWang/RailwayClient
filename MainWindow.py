import sys

from PyQt5 import QtSvg
from PyQt5.QtCore import Qt, pyqtSlot, QRect, QSize, QObject, QTimer
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QWidget, QPushButton, QVBoxLayout, \
    QHBoxLayout, QLCDNumber, QMainWindow
from pyqt_led import Led
import requests
from SideBar import *
from Panel import *
from Graph import *
from Simulator import Simulator


class MainWindow(QWidget):
    data = {}
    user = ''
    url = 'http://192.168.0.108:5000'
    model_chosen = 'None'
    graph_switch = 0
    run_switch = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ini()

    def ini(self):
        self.resize(1080, 720)
        self.setWindowTitle('title')

        # main
        self.main_layout = QHBoxLayout()
        self.side_bar = SideBar()
        self.right = QWidget()
        self.main_layout.addWidget(self.side_bar, 1)
        self.main_layout.addWidget(self.right, 8)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # right
        self.right_layout = QVBoxLayout()
        self.right_layout.setContentsMargins(0, 50, 0, 0)
        self.title = QWidget()
        self.panel = QWidget()
        self.ctrl = QWidget()
        self.right_layout.addWidget(self.title, 1)
        self.right_layout.addWidget(self.panel, 8)
        self.right_layout.addWidget(self.ctrl, 1)
        self.right.setLayout(self.right_layout)

        # title
        self.title_layout = QHBoxLayout()
        self.title_layout.setAlignment(Qt.AlignCenter)
        self.title_layout.setSpacing(40)
        self.title_layout.setContentsMargins(0, 0, 80, 0)
        self.from_lb = QLabel("------站")
        self.from_ico = QtSvg.QSvgWidget('icon/from_ico.svg')
        self.to_lb = QLabel("------站")
        self.to_ico = QtSvg.QSvgWidget('icon/to_ico.svg')
        self.num_lb = QLabel("------")
        self.num_ico = QtSvg.QSvgWidget("icon/num_ico.svg")
        self.driver_lb = QLabel("-------")
        self.driver_ico = QtSvg.QSvgWidget('icon/driver_ico.svg')
        now = QDate.currentDate()
        self.time_ico = QtSvg.QSvgWidget('icon/time_ico.svg')
        self.time_lb = QLabel(now.toString())
        self.from_lb.setStyleSheet('color:white;font:30px')
        self.to_lb.setStyleSheet('color:white;font:30px')
        self.num_lb.setStyleSheet('color:white;font:30px')
        self.driver_lb.setStyleSheet('color:white;font:30px')
        self.time_lb.setStyleSheet('color:white;font:30px')
        self.from_ico.setFixedSize(30, 30)
        self.from_ico.setStyleSheet('background:white;border-radius:10px')
        self.to_ico.setFixedSize(30, 30)
        self.to_ico.setStyleSheet('background:white;border-radius:10px')
        self.num_ico.setFixedSize(30, 30)
        self.num_ico.setStyleSheet('background:white;border-radius:3px')
        self.driver_ico.setFixedSize(30, 35)
        self.driver_ico.setStyleSheet('background:white;border-radius:3px')
        self.time_ico.setFixedSize(30, 30)
        self.time_ico.setStyleSheet('background:white;border-radius:3px')
        self.title_layout.addWidget(self.from_ico)
        self.title_layout.addWidget(self.from_lb)
        self.title_layout.addWidget(self.to_ico)
        self.title_layout.addWidget(self.to_lb)
        self.title_layout.addWidget(self.num_ico)
        self.title_layout.addWidget(self.num_lb)
        self.title_layout.addWidget(self.driver_ico)
        self.title_layout.addWidget(self.driver_lb)
        self.title_layout.addWidget(self.time_ico)
        self.title_layout.addWidget(self.time_lb)
        self.title.setLayout(self.title_layout)

        # ctrl
        self.ctrl_layout = QHBoxLayout()
        # self.ctrl_layout.setAlignment(Qt.AlignVCenter)
        self.ctrl.setContentsMargins(0,0,100,40)
        self.ctrl_bt_list = []
        for i in range(16):
            bt = QPushButton("fn")
            bt.setStyleSheet('color:white;font-size:15px;background:rgb(37,38,74);border-radius:25px')
            bt.setFixedSize(50, 50)
            self.ctrl_bt_list.append(bt)
            self.ctrl_layout.addWidget(bt)
        self.ctrl.setLayout(self.ctrl_layout)

        # panel
        self.panel_layout = QHBoxLayout()
        self.first = QWidget()
        self.second = QWidget()
        self.panel_layout.addWidget(self.first)
        self.panel_layout.addWidget(self.second)
        self.panel.setLayout(self.panel_layout)

        # first
        self.first_layout = QVBoxLayout()
        self.first_layout.setAlignment(Qt.AlignTop)
        self.first.setLayout(self.first_layout)
        self.gpanel = GaugePanel()
        self.gpanel.setFixedSize(520, 360)
        bt_rm = QPushButton("RM")
        bt_CBTC = QPushButton("CBTC")
        bt_AM = QPushButton("AM")
        bt_AA = QPushButton('AA')
        first_bt_list = [bt_rm, bt_CBTC, bt_AM, bt_AA]
        self.pix_label = QLabel()
        self.pix_label.setPixmap(QPixmap('train_pic.png'))
        bt_layout = QHBoxLayout()
        first_bt = QWidget()
        first_bt.setLayout(bt_layout)
        for bt in first_bt_list:
            bt.setStyleSheet('color:white;font-size:25px;background:rgb(37,38,74);border-radius:35px;')
            bt.setFixedSize(70, 70)
            bt_layout.addWidget(bt)
        self.first_layout.addWidget(first_bt)
        self.first_layout.addWidget(self.gpanel)
        self.first_layout.addWidget(self.pix_label)

        # second
        self.second_layout = QGridLayout()
        self.second_layout.setAlignment(Qt.AlignTop)
        self.second_layout.setContentsMargins(0, 0, 100, 0)
        self.second.setLayout(self.second_layout)
        self.graph = Graph()
        self.graph.setStyleSheet('border-radius:70px; border:rgb(7,86,123)')
        self.graph.setFixedSize(640, 480)
        self.second_layout.addWidget(self.graph, 1, 1, 8, 8)
        self.third = QWidget()
        self.second_layout.addWidget(self.third, 9, 1, 9, 8)

        # third
        self.third_layout = QHBoxLayout()
        self.third.setLayout(self.third_layout)
        label1 = QLabel('距离:')
        self.lcd1 = QLCDNumber()
        self.lcd1.setFixedSize(100, 80)
        self.lcd1.setStyleSheet('color:white')
        label2 = QLabel('误差:')
        self.lcd2 = QLCDNumber()
        self.lcd2.setFixedSize(100, 80)
        self.lcd2.setStyleSheet('color:white')
        label3 = QLabel("刹车指令:")
        self.led = Led(parent=self.right, on_color=Led.green, off_color=Led.red, shape=Led.circle, build='release')
        self.led.setFixedSize(20, 30)
        label1.setStyleSheet("font-size:15px;color:white")
        label2.setStyleSheet("font-size:15px;color:white")
        label3.setStyleSheet("font-size:15px;color:white")
        self.lcd1.setSegmentStyle(QLCDNumber.Flat)
        self.lcd2.setSegmentStyle(QLCDNumber.Flat)
        # lcd.setStyleSheet("border: 2px solid black; font-size:40px; color: rgb(58, 130, 246); background: black;")
        self.lcd1.setDigitCount(8)
        self.lcd1.display(0)
        self.lcd2.setDigitCount(8)
        self.lcd2.display(0)
        self.third_layout.addWidget(label1, 1)
        self.third_layout.addWidget(self.lcd1, 2)
        self.third_layout.addWidget(label2, 1)
        self.third_layout.addWidget(self.lcd2, 2)
        self.third_layout.addWidget(label3, 1)
        self.third_layout.addWidget(self.led, 1)

        # style sheet set
        self.setStyleSheet('background:rgb(15,19,38)')

        self.side_bar.run_bt.clicked.connect(self.start_button_clicked)
        self.side_bar.graph_bt.clicked.connect(self.run_graph)

        self.setLayout(self.main_layout)
        self.show()

    def run_graph(self):
        if self.graph_switch == 0:
            self.graph_switch = 1
            self.side_bar.graph_bt.setStyleSheet('background-color:white; color:#1d1c1d;font-size:15px;')
        else:
            self.graph_switch = 0
            self.side_bar.graph_bt.setStyleSheet('background:rgb(27,28,64);color:white;font-size:15px;')

    def start_button_clicked(self):
        if self.run_switch == 0:
            self.side_bar.run_bt.setStyleSheet('background-color:white; color:#1d1c1d;font-size:15px;')
            self.run_switch = 1
            self.model_chosen = self.side_bar.model_cb.get_model()
            self.side_bar.model_cb.lock()
            self.simulator = Simulator()
            self.simulator.set_model(self.model_chosen)
            self.flag = 1
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.run)
            self.timer.start(1000)
        else:
            self.run_switch = 0
            self.side_bar.run_bt.setStyleSheet('background:rgb(27,28,64);color:white;font-size:15px;')
            self.timer.stop()

    def run(self):
        pos, v = self.simulator.emit_data()
        self.gpanel.set_panel_value(v)
        error, hlt = self.predict(pos, v)
        error = float(error)
        hlt = float(hlt)
        if self.graph_switch == 1:
            if self.flag == 1:
                self.graph.myChart.set_range(pos, error)
                self.flag = 0
            self.graph.threading_slot(pos, error)
        print(error)
        self.lcd1.display(pos)
        self.lcd2.display(error)
        if int(hlt) != 0:
            print("hlt")
            self.change_hlt()
        if (len(list(self.simulator.get_all_data().keys()))) == self.simulator.time:
            self.timer.stop()

    def predict(self, pos, v):
        tmp = {'Model': self.model_chosen, 'User': self.user, 'Position': pos, 'Velocity': v}
        text = requests.get(self.url + '/demo_predict/', tmp).text
        ans = text.split(",")
        error = ans[0]
        hlt = ans[1]
        return error, hlt

    def set_url(self, url):
        self.url = url

    def set_user(self, user):
        self.user = user

    def change_hlt(self):
        self.led.turn_on(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
