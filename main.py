# from mainW import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from css_style import Css_Styles
from functools import partial
from PyQt5 import QtGui, QtCore
import sys
import os

__version__ = '1.0.1'

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def createWindow(self, _type):
        page = WebEnginePage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @QtCore.pyqtSlot(QtCore.QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()


class MyLabel(QLabel):
    leftclicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.leftclicked.emit()
        QLabel.mousePressEvent(self, ev)

    def enterEvent(self, event):
        super().enterEvent(event)       
        Css_Styles.set_label_hover_style(self)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        Css_Styles.set_label_style(self)
    

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()        
        self.browser = QtWebEngineWidgets.QWebEngineView()
        page = WebEnginePage(self.browser)
        self.browser.setPage(page)
        
        self.url_map = {
            "Home": "https://bizonbizon.notion.site/Getting-Started-Guide-6956f7a535ed44bdb4ee77e61a88aad5",
            "Guides": "https://www.notion.so/bizonbizon/Bizon-Technical-Support-Portal-a1201a84f86b4797982e06d360351f54",
            "Scripts": "https://bizonbizon.notion.site/Scripts-9f1e07a85f2346ba9ab8a1bdb824df10",
            "AI catalog": "https://catalog.ngc.nvidia.com/?filters=&orderBy=scoreDESC&query=",
            "Bizon apps": "https://bizon-tech.com/bizonos_features",
            "Support": "https://082eee78-4758-4d6f.gradio.live",
            
        }
        self.btns = []
        self.active_tab = "home"        
        self.set_looks()
        self.setWindowIcon(QtGui.QIcon('/usr/local/share/dlbt_os/bza/bizon_app/ico.png'))
        self.setup_web_widget()            
        self.show()
    
    def set_looks(self):
        Css_Styles.set_whole_styles(self,"")
    
    def activate_tab(self, tab, event=None):        
        self.active_tab = tab
        self.update_active_tab()
    
    # def set_bold_font(self,b, ev=None):
    #     print("here")
    #     myFont= QFont()
    #     myFont.setBold(True)
    #     b.setFont(myFont)
        

    def setup_web_widget(self):        
        
        vbox = QVBoxLayout()
        ## Add buttons bar
        hbox = QHBoxLayout()        
                
        hsp1 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hsp2 = QSpacerItem(25, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        self.upd_btn = QLabel()
        self.upd_btn.setMinimumWidth(20)
        self.upd_btn.setMaximumHeight(30)        
        self.upd_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        qp = QPixmap("/usr/local/share/dlbt_os/bza/bizon_app/ico_upd.png")
        self.upd_btn.setPixmap(qp.scaledToHeight(20))
        self.upd_btn.mousePressEvent = self.update_app
        
        for k in self.url_map:
            b = MyLabel(k)
            b.setMinimumWidth(84)
            b.setMaximumHeight(34)
            b.setAlignment(QtCore.Qt.AlignCenter)
            b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            Css_Styles.set_label_style(self)
            # b.enterEvent = partial(self.enterEventL,b)
            # b.leaveEvent = partial(self.leaveEventL,b)
            b.mousePressEvent = partial(self.activate_tab,k)
            self.btns.append(b)    
        
        self.menu_btn = QLabel()
        self.menu_btn.setMinimumWidth(20)
        self.menu_btn.setMaximumHeight(30)
        self.menu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        qp = QPixmap("/usr/local/share/dlbt_os/bza/bizon_app/ico_menu.png")
        self.menu_btn.setPixmap(qp.scaledToHeight(self.menu_btn.height()))
        self.menu_btn.setAlignment(QtCore.Qt.AlignCenter)
        # self.menu_btn.setScaledContents(True)        
        
        hbox.addWidget(self.upd_btn)
        hbox.addSpacerItem(hsp1)
        for b in self.btns:
            hbox.addWidget(b)
        
        hbox.addSpacerItem(hsp2)
        hbox.addWidget(self.menu_btn)
                
        vbox.addLayout(hbox)                
        vbox.addWidget(self.browser)
        
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle("Bizon APP " + __version__)              
        self.setMinimumSize(1000,700)
        self.activate_tab("Home")
           
    def update_app(self, event):
        buttonReply = QMessageBox.question(self, 'Update', "Do you want to update the Bizon App?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:            
            r = os.popen("/usr/local/share/dlbt_os/bza/bizon_app/upd_bza").read()
            msg = QMessageBox(self)
            msg.setMinimumWidth(200)
            msg.setMaximumHeight(100)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Update")
            msg.setInformativeText('Please restart the app to apply the changes.')
            msg.setWindowTitle("Update Successful")
            msg.exec_()
            print(r)
        
    
    def update_active_tab(self):        
        url = QUrl.fromUserInput(self.url_map[self.active_tab])
        self.browser.load(url)
        
if __name__ == "__main__":     
    main_app = QApplication(sys.argv)
    tester = MainWindow()    
    ## For the app for the user
    sys.exit(main_app.exec_())
