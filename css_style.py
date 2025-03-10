
class Css_Styles:
    
    @staticmethod    
    def menu_bar_styles(item):
        item.setStyleSheet("""
            QMenuBar{
                background: #ffffff;
                border-bottom: 1px solid #e0e0e0;
                padding: 4px;
            }
            QMenuBar::item{
                background: transparent;
                color: #424242;
                padding: 6px 10px;
                margin: 1px 4px;
                border-radius: 4px;
            }
            QMenuBar::item:selected{
                background: rgba(53, 99, 233, 0.15);
                color: #3563E9;
            }
            QMenu{
                background: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 4px;
            }
            QMenu::item{
                background: transparent;
                color: #424242;
                padding: 6px 20px;
                margin: 2px 4px;
                border-radius: 4px;
            }
            QMenu::item:selected{
                background: rgba(53, 99, 233, 0.15);
                color: #3563E9;
            }
        """)
        
    @staticmethod
    def set_label_style(item):        
        item.setStyleSheet("""
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 16px;
        font-weight: 500;
        color: #424242; 
        padding: 8px 16px; 
        border-radius: 8px;
        margin: 2px;
        transition: background-color 0.3s;
        """)
        
    @staticmethod
    def set_label_hover_style(item):        
        item.setStyleSheet("""        
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 16px;      
        font-weight: 600;  
        background-color: rgba(53, 99, 233, 0.15);
        color: #3563E9;
        padding: 8px 16px; 
        border-radius: 8px;
        margin: 2px;
        """)
    
    @staticmethod  
    def set_whole_styles(item, background_path):
        item.setStyleSheet("""  
            QMainWindow {
                background: #f5f5f7;
                border-radius: 10px;
                background-repeat: no-repeat; 
                background-position: center;
            }
            QMenuBar{
                background: #ffffff;
                border-bottom: 1px solid #e0e0e0;
                padding: 8px;
            }
            QStatusBar{
                color: #424242;
                background: #ffffff;
                border-top: 1px solid #e0e0e0;
                padding: 4px;
            }            

            QPushButton {
                background-color: #3563E9;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background-color: #2954d0;
            }
            
            QPushButton:pressed {
                background-color: #1e47c3;    
            }
            
            QWebEngineView{
                border-radius: 8px; 
                border: 1px solid #e0e0e0;
                background: #ffffff;
            }
            
            QLabel {
                color: #424242;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QScrollBar:vertical {
                border: none;
                background: #f5f5f7;
                width: 10px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """.replace("$BACKPATH",background_path))

    @staticmethod
    def danger_style(item):
        item.setStyleSheet("""
            color: #e53935;
            font-weight: 500;
            padding: 8px;
            background-color: rgba(229, 57, 53, 0.1);
            border-radius: 4px;
        """)

    @staticmethod
    def success_style(item):
        item.setStyleSheet("""
            color: #43a047;
            font-weight: 500;
            padding: 8px;
            background-color: rgba(67, 160, 71, 0.1);
            border-radius: 4px;
        """)