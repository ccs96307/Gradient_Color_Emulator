# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gradient import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Display color
        self.ui.color_1.setStyleSheet('background-color: rgb(0, 0, 0);')
        self.ui.color_2.setStyleSheet('background-color: rgb(0, 0, 0);')

        # HorizontalSlider
        self.ui.horizontalSlider.setMaximum(255)
        self.ui.horizontalSlider_2.setMaximum(255)
        self.ui.horizontalSlider_3.setMaximum(255)
        self.ui.horizontalSlider_4.setMaximum(255)
        self.ui.horizontalSlider_5.setMaximum(255)
        self.ui.horizontalSlider_6.setMaximum(255)

        self.ui.horizontalSlider.valueChanged.connect(lambda: self.color_value('R1'))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.color_value('G1'))
        self.ui.horizontalSlider_3.valueChanged.connect(lambda: self.color_value('B1'))
        self.ui.horizontalSlider_4.valueChanged.connect(lambda: self.color_value('R2'))
        self.ui.horizontalSlider_5.valueChanged.connect(lambda: self.color_value('G2'))
        self.ui.horizontalSlider_6.valueChanged.connect(lambda: self.color_value('B2'))

        # Shortcut
        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)

    def color_value(self, color):
        if color == 'R1':
            self.ui.lineEdit.setText(str(self.ui.horizontalSlider.value()))
        elif color == 'G1':
            self.ui.lineEdit_2.setText(str(self.ui.horizontalSlider_2.value()))
        elif color == 'B1':
            self.ui.lineEdit_3.setText(str(self.ui.horizontalSlider_3.value()))
        elif color == 'R2':
            self.ui.lineEdit_4.setText(str(self.ui.horizontalSlider_4.value()))
        elif color == 'G2':
            self.ui.lineEdit_5.setText(str(self.ui.horizontalSlider_5.value()))
        elif color == 'B2':
            self.ui.lineEdit_6.setText(str(self.ui.horizontalSlider_6.value()))

        self.color_change()

    def color_change(self):
        self.newR1 = int(self.ui.lineEdit.text())
        self.newG1 = int(self.ui.lineEdit_2.text())
        self.newB1 = int(self.ui.lineEdit_3.text())
        self.ui.color_1.setStyleSheet('background-color: rgb({}, {}, {});'.format(
            self.newR1,
            self.newG1,
            self.newB1
        ))
        self.newR2 = int(self.ui.lineEdit_4.text())
        self.newG2 = int(self.ui.lineEdit_5.text())
        self.newB2 = int(self.ui.lineEdit_6.text())
        self.ui.color_2.setStyleSheet('background-color: rgb({}, {}, {});'.format(
            self.newR2,
            self.newG2,
            self.newB2
        ))

        self.gradient_color_button()

    def gradient_color_button(self):
        self.ui.pushButton.setStyleSheet('background-color: '
                                         'qlineargradient('
                                         'spread:'
                                         'pad, x1:0, y1:0.5, x2:1, y2:0.5,'
                                         'stop:0 rgb({}, {}, {}),'
                                         'stop:1 rgb({}, {}, {}));'.format(self.newR1,
                                                                           self.newG1,
                                                                           self.newB1,
                                                                           self.newR2,
                                                                           self.newG2,
                                                                           self.newB2))

    def exitEvent(self):
        exit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())