import threading
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon,QApplication
from PyQt5.QtGui import QIcon
import sys
import subprocess

def call_boost(toggle_state):
    if toggle_state == True:
        subprocess.Popen(["powercfg", "-setacvalueindex", "scheme_current", "sub_processor",
                          "5d76a2ca-e8c0-402f-a133-2158492d58ad", "1"],creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.Popen(["powercfg", "-setactive", "scheme_current"],creationflags=subprocess.CREATE_NO_WINDOW)
    if toggle_state == False:
        subprocess.Popen(["powercfg", "-setacvalueindex", "scheme_current", "sub_processor",
                          "5d76a2ca-e8c0-402f-a133-2158492d58ad", "0"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.Popen(["powercfg", "-setactive", "scheme_current"], creationflags=subprocess.CREATE_NO_WINDOW)

subprocess.Popen(["powercfg", "-setacvalueindex", "scheme_current", "sub_processor",
                          "5d76a2ca-e8c0-402f-a133-2158492d58ad", "0"], creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(["powercfg", "-setactive", "scheme_current"], creationflags=subprocess.CREATE_NO_WINDOW)

toggle_state = False
def onDoubleClick(reason):
    global toggle_state,tray_icon
    if reason == QSystemTrayIcon.DoubleClick:
        toggle_state = not toggle_state
        threading.Thread(target=lambda: call_boost(toggle_state), daemon=True).start()
        if toggle_state == False:
            tray_icon.setIcon(QIcon(r'Dependancy\\Resources\\off.ico'))
        elif toggle_state == True:
            tray_icon.setIcon(QIcon(r'Dependancy\\Resources\\on.ico'))
def close_tray_icon():
    app.exit()
    sys.exit()

app = QApplication(sys.argv)
tray_icon = QSystemTrayIcon()
tray_icon.setToolTip("Lock CPU Boost")
tray_icon.setIcon(QIcon(r'Dependancy\\Resources\\off.ico'))
menu = QMenu()
menu.addAction("Exit").triggered.connect(lambda: close_tray_icon())
tray_icon.activated.connect(onDoubleClick)
tray_icon.setContextMenu(menu)
tray_icon.show()
app.exec_()