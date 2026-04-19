import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
from utils import request
import json

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
        
        response = request("Odesa")
        print(json.dumps(response, indent = 4))
        
        
        self.CETRAL_FRAME = widgets.QFrame(self)
        self.CETRAL_FRAME.setFixedSize(788, 303)
        self.CETRAL_FRAME.setStyleSheet("background-color: grey")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.CETRAL_FRAME)
        
        self.CENTRAL_LAYOUT = widgets.QHBoxLayout(self.CETRAL_FRAME)
        self.CETRAL_FRAME.setLayout(self.CENTRAL_LAYOUT)

        self.LABEL = widgets.QLabel(self.CETRAL_FRAME,text = str(response["main"]["temp"]))
        self.CENTRAL_LAYOUT.addWidget(self.LABEL)
        
        self.FOOTER = widgets.QFrame(parent = self)
        self.FOOTER.setFixedSize(788, 364)
        self.FOOTER.setStyleSheet("background-color: grey")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.FOOTER)
