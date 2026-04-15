import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import requests
import json

from .app import application
from .left_container import LeftContainer
from .weather_container import WeatherContainer


city_name = "Dnipro"
API_key = "4d5a216bd76d84e8f7528002428d53ff"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
print(response.json())

print("\n", json.dumps(response.json(), indent= 4))



class MainWindow(widgets.QMainWindow):
    def __init__(self):
        super().__init__()

        
        window_width = 1200
        window_height = 800

        screen = application.primaryScreen()
        screen_size = screen.size()

        screen_width = screen_size.width()
        screen_height = screen_size.height()

        center_x = (screen_width // 2) - (window_width // 2)
        center_y = (screen_height // 2) - (window_height // 2)

        self.setGeometry(center_x, center_y, window_width, window_height)
        self.setWindowTitle("Project")

        central_widget = widgets.QWidget(self)
        central_widget.setFixedSize(1200,800  )

        center_widget_layout = widgets.QHBoxLayout()
        center_widget_layout.setSpacing(0)
        center_widget_layout.setContentsMargins(0, 0, 0, 0)
        
        
        central_widget.setLayout(center_widget_layout)
        
        self.LEFT_CONTAINER = LeftContainer(parent = central_widget)
        self.WEATHER_CONTAINER = WeatherContainer(parent = central_widget)
        
        center_widget_layout.addWidget(self.LEFT_CONTAINER)
        center_widget_layout.addWidget(self.WEATHER_CONTAINER)
    
    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.RightButton:
            print("Правая кнопка")
    
    def keyPressEvent(self, event: gui.QKeyEvent):
        if event.key() == core.Qt.Key.Key_K:
            print(event.text())
            print(event.key())      
    
    def mouseReleaseEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.RightButton:
            print("right: works")
    
    def keyReleaseEvent(self, event: gui.QKeyEvent):
        if event.key() == core.Qt.Key.Key_K:
            print(f"Key: {event.key()}")
            print(f"Text: {event.text()}")
        

main_window = MainWindow()
