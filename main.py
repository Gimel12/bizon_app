# from mainW import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from css_style import Css_Styles
import sys
from functools import partial


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.webEngineView = QWebEngineView()
        self.url_map = {
            "Home": "https://bizonbizon.notion.site/Getting-Started-Guide-6956f7a535ed44bdb4ee77e61a88aad5",
            "Guides": "https://www.notion.so/bizonbizon/Bizon-Technical-Support-Portal-a1201a84f86b4797982e06d360351f54",
            "Scripts": "https://bizonbizon.notion.site/Scripts-9f1e07a85f2346ba9ab8a1bdb824df10",
            "Bizon AI": "www.nvidia.com",
            "Support": "www.nvidia.com",
        }
        self.btns = []
        self.active_tab = "home"        
        self.set_looks()
        self.setup_web_widget()            
        self.show()
    
    def set_looks(self):
        Css_Styles.set_whole_styles(self,"")
    
    def activate_tab(self, tab, event=None):        
        self.active_tab = tab
        self.update_active_tab()
    
    def setup_web_widget(self):        
        
        vbox = QVBoxLayout()
        ## Add buttons bar
        hbox = QHBoxLayout()
        self.bt = ["home", "guides", "script", "bizon_ai", "support"]
        
        for k in self.url_map:
            b = QLabel(k)
            b.setMinimumWidth(100)
            b.setMaximumHeight(40)
            b.mousePressEvent = partial(self.activate_tab,k)
            self.btns.append(b)    
        
        for b in self.btns:
            hbox.addWidget(b)
        vbox.addLayout(hbox)                
        vbox.addWidget(self.webEngineView)
        
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle("Bizon APP")        
        self.setMinimumSize(1000,700)
        self.activate_tab("Home")
           
    
    def update_active_tab(self):
        url = QUrl.fromUserInput(self.url_map[self.active_tab])
        self.webEngineView.load(url)
        
if __name__ == "__main__":     
    main_app = QApplication(sys.argv)
    tester = MainWindow()    
    ## For the app for the user
    sys.exit(main_app.exec_())