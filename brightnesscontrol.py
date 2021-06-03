import sys
import os
import threading

import screen_brightness_control as sbc

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QSlider, QWidgetAction, QAction

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Adding an icon
icon = QIcon(resource_path("icon.ico"))

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options
menu = QMenu()

brightnessControl = QSlider(Qt.Vertical)
brightnessControl.setValue(100)
brightnessControl.setMaximum(20)

# menu.addActions(mySlider)


def valuechange():
    value = brightnessControl.value()*5
    x = threading.Thread(target=sbc.set_brightness, args=(value,), daemon=True)
    x.start()



widgetSlider = QWidgetAction(brightnessControl)
widgetSlider.setDefaultWidget(brightnessControl)
menu.addAction(widgetSlider)
brightnessControl.sliderMoved.connect(valuechange)


# To quit the app
menu2 = QMenu()
quit = QAction("X")
quit.triggered.connect(app.quit)
menu2.addAction(quit)

menu.addMenu(menu2)

# Adding options to the System Tray
tray.setContextMenu(menu)

sys.exit(app.exec())