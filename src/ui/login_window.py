from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt
import os
from dotenv import load_dotenv

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(400, 250)  # Изменённый размер окна

        # Загрузка логина и пароля из файла .env
        load_dotenv()
        self.correct_username = os.getenv("USERNAME")
        self.correct_password = os.getenv("PASSWORD")

        # Проверка, что логин и пароль загружены
        if not self.correct_username or not self.correct_password:
            self.show_message("Ошибка конфигурации", "Логин или пароль не загружены из .env", QMessageBox.Icon.Critical)

        # Основной макет
        layout = QVBoxLayout()

        # Поле ввода имени пользователя
        self.username_label = QLabel("Имя пользователя:")
        layout.addWidget(self.username_label)
        self.username_input = QLineEdit()
        self.username_input.setFixedSize(250, 40)  # Установка фиксированного размера
        self.username_input.setStyleSheet("QLineEdit { padding: 5px; font-size: 14px; }")  # Добавление стиля
        layout.addWidget(self.username_input)

        # Поле ввода пароля
        self.password_label = QLabel("Пароль:")
        layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setFixedSize(250, 40)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("QLineEdit { padding: 5px; font-size: 14px; }")
        layout.addWidget(self.password_input)

        # Кнопка авторизации
        self.login_button = QPushButton("Войти")
        self.login_button.setFixedSize(150, 40)  # Изменён размер кнопки
        self.login_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 16px; padding: 8px; }")
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Установка макета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def check_login(self):
        # Получение введённых данных
        username = self.username_input.text()
        password = self.password_input.text()

        # Проверка логина и пароля
        if username == self.correct_username and password == self.correct_password:
            self.show_message("Успешная авторизация", "Добро пожаловать!", QMessageBox.Icon.Information)
            self.open_main_window()  # Открытие главного окна
        else:
            self.show_message("Ошибка", "Неверные имя пользователя или пароль", QMessageBox.Icon.Critical)

    def show_message(self, title, text, icon):
        # Всплывающее окно с сообщением
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.exec()

    def open_main_window(self):
        # Логика для открытия главного окна
        print("Открываем главное окно")
        # Здесь можно вызвать основное окно интерфейса, если оно есть:
        # self.main_window = MainWindow() 
        # self.main_window.showFullScreen()  # Открытие на полный экран

# Временно отключаем окно авторизации
#login_window = LoginWindow()
#login_window.show()