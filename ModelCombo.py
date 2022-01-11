import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication, QListView
from qt_material import apply_stylesheet

class ModelCombo(QWidget):
    def __init__(self):
        super(ModelCombo, self).__init__()
        self.ini()

    def ini(self):
        self.cb = QComboBox(self)
        self.cb.addItems(['NRM', 'DNN', 'CNN', 'FSCNN'])
        self.model = self.cb.currentText()
        self.cb.setFixedSize(100, 40)
        self.cb.setView(QListView())
        self.unlock()
        self.cb.currentIndexChanged[str].connect(self.change_model)
        self.setStyleSheet('color:white;border:white')

    def change_model(self, m):
        self.model = m
        print(self.model)

    def get_model(self):
        return self.model

    def unlock(self):
        self.cb.setEnabled(True)

    def lock(self):
        self.cb.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cb = ModelCombo()
    cb.show()

    sys.exit(app.exec_())

