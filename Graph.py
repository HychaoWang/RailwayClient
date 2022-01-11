import random
import math
import time
import threading

from PyQt5.QtChart import (QAreaSeries, QBarSet, QChart, QChartView,
                           QLineSeries, QPieSeries, QScatterSeries, QSplineSeries,
                           QStackedBarSeries, QValueAxis)
from PyQt5.QtCore import (
    pyqtSlot, QPoint, QPointF, Qt, QTimer
)
from PyQt5.Qt import (QApplication, QWidget, QPushButton,
                      QThread, QMutex, pyqtSignal)
from PyQt5.QtGui import QColor, QPainter, QPalette
from PyQt5.QtWidgets import (QCheckBox, QComboBox, QGridLayout, QHBoxLayout,
                             QLabel, QSizePolicy, QWidget, QPushButton)
from Simulator import *


class TestChart(QChart):
    def __init__(self, parent=None):
        super(TestChart, self).__init__(parent)
        self.sampleRate = 1
        self.counter = 0
        self.seriesList = []
        self.legend().show()

        self.axisX = QValueAxis()
        self.addAxis(self.axisX, Qt.AlignBottom)
        # self.setAxisX(self.axisX, series)

        self.axisY = QValueAxis()
        self.addAxis(self.axisY, Qt.AlignLeft)
        # self.setAxisY(self.axisY, series)

        self.series = QLineSeries()
        self.series.setName("停车误差线")
        self.series.setColor(Qt.yellow)
        self.series.setBrush(Qt.white)
        self.series.setUseOpenGL(True)
        self.addSeries(self.series)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)

        self.axisX.setLabelsColor(Qt.white)
        self.axisY.setLabelsColor(Qt.white)
        self.setBackgroundBrush(QColor(26,30,62))
        self.setTitleBrush(Qt.white)

    def handleUpdate(self, x, y):
        self.series.append(x, y)
        self.series.setUseOpenGL(True)

    def set_range(self, x, y):
        self.axisX.setRange(float(-1*x/5), float(x))
        self.axisX.setReverse(True)
        self.axisY.setRange(float(-1*y/5), float(y))


class Graph(QWidget):

    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)

        # Create the layout.
        baseLayout = QGridLayout()
        settingsLayout = QHBoxLayout()
        settingsLayout.addStretch()
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        self.myChart = TestChart()
        self.myChart.setTheme(QChart.ChartThemeBlueCerulean)
        chartView = QChartView(self.myChart)
        chartView.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        baseLayout.addWidget(chartView)
        # self.m_charts.append(chartView)
        self.setLayout(baseLayout)

    def threading_slot(self, x, y):
        print(x, y)
        print(type(x),type(y))
        self.myChart.handleUpdate(float(x), float(y))
        # 实时刷新界面
        QApplication.processEvents()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    window = QMainWindow()
    widget = Graph()
    window.setCentralWidget(widget)
    window.resize(900, 600)
    window.show()
    sys.exit(app.exec_())
