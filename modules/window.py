import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

from .app import application


main_window = widgets.QMainWindow()

window_width = 1200
window_height = 800

screen = application.primaryScreen()
screen_size = screen.size()

screen_width = screen_size.width()
screen_height = screen_size.height()

center_x = (screen_width // 2) - (window_width // 2)
center_y = (screen_height // 2) - (window_height // 2)

main_window.setGeometry(center_x, center_y, window_width, window_height)
main_window.setWindowTitle("Project")

# Богдан
# Создать центральный виджет, указать в родителе окно
central_widget = widgets.QWidget(main_window)
central_widget.setFixedSize(1200,800  )

# Никита
# Создать лейаут для центр. виджета, прикрепить этот лейаут (к нему)
center_widget_layout = widgets.QGridLayout()
central_widget.setLayout(center_widget_layout)

# Кирилл
# Создать кнопку, указать размеры, стилизовать
# button = widgets.QPushButton(parent = central_widget)
# button.setFixedSize(80, 60)
# button.setStyleSheet("background-color: black; border: 5px solid red")
# center_widget_layout.addWidget(button)

# Женя
# Создать поле ввода, обработать сигнал ввода текста
# line = widgets.QLineEdit(parent = central_widget)
# line.setPlaceholderText("Enter text")
# line.setFixedSize(500, 500)


# def line_changed():
#     print(line.text())
# line.textChanged.connect(line_changed)
# center_widget_layout.addWidget(line)


# Назар
# Создать фрейм, создать лейаут (для фрейма), прикрепить лейаут к фрейму
# frame = widgets.QFrame()
# frame_layout = widgets.QVBoxLayout()
# center_widget_layout.addWidget(frame)

# Полина
# Создать выпадающее меню, добавить туда 2 опции
# dropdownmenu = widgets.QComboBox(parent= central_widget)
# center_widget_layout.addWidget(dropdownmenu)
# dropdownmenu.addItem("Dnipro")
# dropdownmenu.addItem("Odessa")
# dropdownmenu.addItem("Kyiv")

# Максим
# Обработать сигнал клика по кнопке button

# def button_click():
#     print("Кнопка нажата")
    
# button.clicked.connect(button_click)

# Егор Столяров
# Создать радио-кнопку, обработать ее сигнал pressed

radio_button = widgets.QRadioButton(parent = central_widget)
center_widget_layout.addWidget(radio_button)

def hello_world():
    print("Hello world")

radio_button.pressed.connect(hello_world)



line = widgets.QTextEdit(parent = central_widget)
center_widget_layout.addWidget(line)

line.toPlainText()
line.toHtml()