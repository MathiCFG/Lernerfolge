import sys
from qtpy import QtWidgets
from QtUi import mainwindow

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

ui_window = mainwindow.Ui_MainWindow()
ui_window.setupUi(window)

window.show()

sys.exit(app.exec_())