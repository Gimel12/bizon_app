# from mainW import Ui_MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QIcon, QFont, QAction, QCursor
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import QUrl
from PyQt6.QtCore import QObject, pyqtSignal, Qt
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile, QWebEngineSettings
from css_style import Css_Styles
from functools import partial
import sys
import os
import tempfile

__version__ = '1.0.1'

class WebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set a desktop user agent to avoid mobile redirects
        self.profile().setHttpUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Configure settings to better handle Notion pages
        settings = self.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        
        # Enable cookies
        self.profile().setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)
        
        # Create a cookie store directory if it doesn't exist
        cookie_dir = os.path.join(tempfile.gettempdir(), "bizon_app_cookies")
        if not os.path.exists(cookie_dir):
            os.makedirs(cookie_dir)
        self.profile().setPersistentStoragePath(cookie_dir)
        
        # Additional settings for Notion pages
        # Enable DNS prefetching for better performance
        settings.setAttribute(QWebEngineSettings.WebAttribute.DnsPrefetchEnabled, True)
        # Allow cross-origin requests which is needed for Notion
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        # Allow running insecure content (http content in https pages)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        
    def createWindow(self, _type):
        page = WebEnginePage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @QtCore.pyqtSlot(QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()
        
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        # Uncomment for debugging
        pass
        # print(f"JS Console ({level}): {message} [Line: {lineNumber}] [Source: {sourceID}]")


class MyLabel(QLabel):
    leftclicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
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
        
        # Create a custom profile for the browser
        profile = QWebEngineProfile("bizon_app_profile")
        profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)
        profile.setHttpUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Create cache directory if it doesn't exist
        cache_dir = os.path.expanduser("~/.bizon_app_cache")
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        profile.setPersistentStoragePath(cache_dir)
        
        # Create browser view and page
        self.browser = QWebEngineView()
        page = WebEnginePage(self)
        
        # Set up the page to handle Notion sites
        # Note: XSSAuditingEnabled is deprecated in Qt6
        # Configure settings to better handle Notion pages
        page.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        page.settings().setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        
        self.browser.setPage(page)
        
        self.url_map = {
            "Home": "https://bizonbizon.notion.site/Getting-Started-Guide-6956f7a535ed44bdb4ee77e61a88aad5?pvs=4",
            "Guides": "https://www.notion.so/bizonbizon/Bizon-Technical-Support-Portal-a1201a84f86b4797982e06d360351f54",
            "Scripts": "https://bizonbizon.notion.site/Scripts-9f1e07a85f2346ba9ab8a1bdb824df10",
            "AI catalog": "https://catalog.ngc.nvidia.com/?filters=&orderBy=scoreDESC&query=",
            "Bizon apps": "https://bizon-tech.com/bizonos_features",
            "Support": "https://www.youtube.com/"
            
        }
        self.btns = []
        self.active_tab = "home"        
        self.set_looks()
        self.setWindowIcon(QIcon('/usr/local/share/dlbt_os/bza/bizon_app/ico.png'))
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
        # Create navigation bar
        nav_bar = QHBoxLayout()
        
        # Back button
        self.back_btn = QPushButton()
        self.back_btn.setIcon(QIcon.fromTheme("go-previous"))
        self.back_btn.setToolTip("Go Back")
        self.back_btn.setFixedSize(30, 30)
        self.back_btn.clicked.connect(self.go_back)
        
        # Forward button
        self.forward_btn = QPushButton()
        self.forward_btn.setIcon(QIcon.fromTheme("go-next"))
        self.forward_btn.setToolTip("Go Forward")
        self.forward_btn.setFixedSize(30, 30)
        self.forward_btn.clicked.connect(self.go_forward)
        
        # Refresh button
        self.refresh_btn = QPushButton()
        self.refresh_btn.setIcon(QIcon.fromTheme("view-refresh"))
        self.refresh_btn.setToolTip("Refresh")
        self.refresh_btn.setFixedSize(30, 30)
        self.refresh_btn.clicked.connect(self.refresh_page)
        
        # Home button
        self.home_btn = QPushButton()
        self.home_btn.setIcon(QIcon.fromTheme("go-home"))
        self.home_btn.setToolTip("Home")
        self.home_btn.setFixedSize(30, 30)
        self.home_btn.clicked.connect(lambda: self.activate_tab("Home"))
        
        # Add navigation buttons to layout
        nav_bar.addWidget(self.back_btn)
        nav_bar.addWidget(self.forward_btn)
        nav_bar.addWidget(self.refresh_btn)
        nav_bar.addWidget(self.home_btn)
        nav_bar.addStretch(1)
        
        # Main horizontal layout for tabs
        hbox = QHBoxLayout()        
                
        hsp1 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        hsp2 = QSpacerItem(25, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        
        self.upd_btn = QLabel()
        self.upd_btn.setMinimumWidth(20)
        self.upd_btn.setMaximumHeight(30)        
        self.upd_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        qp = QPixmap("/usr/local/share/dlbt_os/bza/bizon_app/ico_upd.png")
        self.upd_btn.setPixmap(qp.scaledToHeight(20))
        self.upd_btn.mousePressEvent = self.update_app
        
        for k in self.url_map:
            b = MyLabel(k)
            b.setMinimumWidth(84)
            b.setMaximumHeight(34)
            b.setAlignment(Qt.AlignmentFlag.AlignCenter)
            b.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            Css_Styles.set_label_style(self)
            # b.enterEvent = partial(self.enterEventL,b)
            # b.leaveEvent = partial(self.leaveEventL,b)
            b.mousePressEvent = partial(self.activate_tab,k)
            self.btns.append(b)    
        
        self.menu_btn = QLabel()
        self.menu_btn.setMinimumWidth(20)
        self.menu_btn.setMaximumHeight(30)
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        qp = QPixmap("/usr/local/share/dlbt_os/bza/bizon_app/ico_menu.png")
        self.menu_btn.setPixmap(qp.scaledToHeight(self.menu_btn.height()))
        self.menu_btn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.menu_btn.setScaledContents(True)        
        
        hbox.addWidget(self.upd_btn)
        hbox.addSpacerItem(hsp1)
        for b in self.btns:
            hbox.addWidget(b)
        
        hbox.addSpacerItem(hsp2)
        hbox.addWidget(self.menu_btn)
                
        vbox.addLayout(nav_bar)
        vbox.addLayout(hbox)                
        vbox.addWidget(self.browser)
        
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle("Bizon APP " + __version__)              
        self.setMinimumSize(1000,700)
        self.activate_tab("Home")
           
    def update_app(self, event):
        buttonReply = QMessageBox.question(self, 'Update', "Do you want to update the Bizon App?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if buttonReply == QMessageBox.StandardButton.Yes:
            # Get the path to the upd_bza.py script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            update_script = os.path.join(current_dir, 'upd_bza.py')
            
            # Run the update script
            try:
                import subprocess
                result = subprocess.run([sys.executable, update_script], capture_output=True, text=True)
                success = result.returncode == 0
                output = result.stdout
                error = result.stderr
                
                # Show appropriate message based on success/failure
                msg = QMessageBox(self)
                msg.setMinimumWidth(300)
                msg.setMaximumHeight(200)
                
                if success:
                    msg.setIcon(QMessageBox.Icon.Information)
                    msg.setText("Update Successful")
                    msg.setInformativeText('Please restart the app to apply the changes.')
                    msg.setWindowTitle("Update Successful")
                    print("Update successful:\n", output)
                else:
                    msg.setIcon(QMessageBox.Icon.Warning)
                    msg.setText("Update Failed")
                    msg.setInformativeText(f'Error updating the app: {error}')
                    msg.setWindowTitle("Update Failed")
                    print("Update failed:\n", error)
                
                msg.exec()
            except Exception as e:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Update Error")
                msg.setInformativeText(f'An error occurred while updating: {str(e)}')
                msg.setWindowTitle("Update Error")
                msg.exec()
                print(f"Update error: {str(e)}")
        
    
    def update_active_tab(self):        
        url = QUrl.fromUserInput(self.url_map[self.active_tab])
        # Load the URL directly - we'll handle Notion pages through the WebEnginePage class
        self.browser.load(url)
    
    def go_back(self):
        self.browser.back()
        
    def go_forward(self):
        self.browser.forward()
        
    def refresh_page(self):
        self.browser.reload()
        
if __name__ == "__main__":     
    main_app = QApplication(sys.argv)
    tester = MainWindow()    
    ## For the app for the user
    sys.exit(main_app.exec())
