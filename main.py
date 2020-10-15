from PySide2 import QtCore, QtGui, QtWidgets
import gui, sys, os
from random import randint
from datetime import datetime


class MainWindow(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        QtWidgets.QMainWindow.__init__(self)
        gui.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ReColor)
        self.saveButton.clicked.connect(self.OnSaveButton)
        self.saveButton.setEnabled(False)
        self.InitButtonSettings(self.linelockButton)
        self.InitButtonSettings(self.line2lockButton)
        self.InitButtonSettings(self.line3lockButton)
        self.InitButtonSettings(self.windowlockButton)

    def InitButtonSettings(self, button: QtWidgets.QPushButton):
        button.clicked.connect(lambda: self.ChangeLockButtonState(button))
        button.setEnabled(False)

    def ChangeLockButtonState(self, button: QtWidgets.QPushButton):
        if button.text() == 'U':
            button.setText('L')
        elif button.text() == 'L':
            button.setText('U')

    def ButtonGroupVisible(self, val: bool):
        if val is True:
            for button in self.lockbuttonGroup.buttons():
                button.show()
        elif val is False:
            for button in self.lockbuttonGroup.buttons():
                button.hide()
        QtWidgets.QApplication.processEvents()

    def ReColorLine(self, button: QtWidgets.QPushButton, line: QtWidgets.QLineEdit):
        if button.text() == 'U':
            line.setStyleSheet(f"""QLineEdit {{ background-color: rgb({self.RandomColor()}, {self.RandomColor()}, {self.RandomColor()}); color: rgb({self.RandomColor()}, {self.RandomColor()}, {self.RandomColor()}) }}""")
            line.setText(f'BG {line.palette().color(QtGui.QPalette.Background).getRgb()[:3]} Text {line.palette().text().color().getRgb()[:3]}')
        elif button.text() == 'L':
            pass

    def ReColorWindow(self):
        if self.windowlockButton.text() == 'U':
            self.setStyleSheet(f"""QMainWindow {{ background-color: rgb({self.RandomColor()}, {self.RandomColor()}, {self.RandomColor()}) }}""")
            self.label.setStyleSheet(f"""QLabel {{ color: rgb({self.RandomColor()}, {self.RandomColor()}, {self.RandomColor()}) }}""")
            self.label.setText(f'BG {self.palette().color(QtGui.QPalette.Background).getRgb()[:3]} Text {self.label.palette().text().color().getRgb()[:3]}')
        elif self.windowlockButton.text() == 'L':
            pass

    def ReColor(self):
        self.saveButton.setEnabled(True)
        self.ReColorLine(self.linelockButton, self.lineEdit)
        self.linelockButton.setEnabled(True)
        self.ReColorLine(self.line2lockButton, self.lineEdit2)
        self.line2lockButton.setEnabled(True)
        self.ReColorLine(self.line3lockButton, self.lineEdit3)
        self.line3lockButton.setEnabled(True)
        self.ReColorWindow()
        self.windowlockButton.setEnabled(True)

    def OnSaveButton(self):
        self.ButtonGroupVisible(False)
        self.Save()
        self.ButtonGroupVisible(True)

    def Save(self):
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save(f'shot_{datetime.now().strftime("%d%m%Y%H%M%S")}.png', 'png')
        with open('shots.txt', 'a+') as txtfile:
            txtfile.write(f'{datetime.now().strftime("%d.%m.%Y %H:%M:")}\nLineEdit 1 {self.lineEdit.text()}\nLineEdit 2 {self.lineEdit2.text()}\nLineEdit 3 {self.lineEdit3.text()}\nWindow {self.label.text()}\n')
            txtfile.close()

    def RandomColor(self):
        colorcode = randint(0, 255)
        return colorcode


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())