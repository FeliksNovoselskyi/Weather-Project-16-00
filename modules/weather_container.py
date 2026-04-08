import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

class WeatherContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(828, 800)
        self.setStyleSheet("background-color: cyan")
        
        self.WEATHER_CONTEINER_LAYOUT = widgets.QVBoxLayout(self)
        self.setLayout(self.WEATHER_CONTEINER_LAYOUT)
        
        self.TOP_FRAME = widgets.QFrame(self)
        self.TOP_FRAME.setFixedSize(788, 36)
        self.TOP_FRAME.setStyleSheet("background-color: grey")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.TOP_FRAME)
        
        self.CETRAL_FRAME = widgets.QFrame(self)
        self.CETRAL_FRAME.setFixedSize(788, 303)
        self.CETRAL_FRAME.setStyleSheet("background-color: grey")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.CETRAL_FRAME)
        
        self.FOOTER = widgets.QFrame(parent = self)
        self.FOOTER.setFixedSize(788, 364)
        self.FOOTER.setStyleSheet("background-color: grey")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.FOOTER)
