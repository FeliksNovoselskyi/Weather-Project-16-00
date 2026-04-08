import PyQt6.QtWidgets as widgets

class LeftContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(370, 800)
        self.setStyleSheet("background-color: red")
