import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
from .app import application
from .left_container import LeftContainer
from .weather_container import WeatherContainer


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
        if event.button() == core.Qt.MouseButton.LeftButton:
            print("LeftButton")
    
    def mouseMoveEvent(self, event: gui.QMouseEvent):
        position = event.position()
        # print(position.toPoint())

    def mouseReleaseEvent(self, event: gui.QMouseEvent):
        print(event.button())

    def keyPressEvent(self, event: gui.QKeyEvent):
        if event.key() == core.Qt.Key.Key_Return or event.key() == core.Qt.Key.Key_Enter:
            print("re")
        

main_window = MainWindow()
