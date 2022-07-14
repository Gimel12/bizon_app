
class Css_Styles:
    
    @staticmethod    
    def menu_bar_styles(item):
        item.setStyleSheet("""
            QMenuBar{
                background: rgb(58,58,58);
            }
            QMenuBar::item{
                background: rgb(88,88,88);
                color: white;
            }
            QMenu{
                background: rgb(88,88,88);
            }
            QMenu::item{
                background: rgb(88,88,88);
                color: white;
            }
        """)
        
    @staticmethod
    def set_label_style(item):        
        item.setStyleSheet("""
        font-family: UnDinaru;
        font-size: 18px;
        font-weight: 500;
        color : #424242; padding: 5px 10px; border-radius: 15px;
        """)
        
    @staticmethod
    def set_label_hover_style(item):        
        item.setStyleSheet("""        
        font-family: UnDinaru;
        font-size: 18px;      
        font-weight: 1500;  
        background-color: rgba(0,57,156,0.25);
        color: #3563E9;
        """)
    
    @staticmethod  
    def set_whole_styles(item, background_path):
        item.setStyleSheet("""  
            QMainWindow {
                background: #D9D9D9;
                border-radius: 20px;
                background-repeat: no-repeat; 
                background-position: center;
            }
            QMenuBar{
                background: rgb(0,0,0);
            }
            QStatusBar{
                color: white;
            }            

            QPushButton:pressed {
                background-color: rgba(89,125,89,1.0);    
            }
            
            QWebEngineView{
                border-radius: 20px; border: 1px solid black;
            }
        """.replace("$BACKPATH",background_path))

    @staticmethod
    def danger_style(item):
        item.setStyleSheet("""
            color: red;
        """)

    @staticmethod
    def success_style(item):
        item.setStyleSheet("""
            color: green;
        """)