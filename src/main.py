import sys
from PyQt6.QtWidgets import QApplication
from ui.login_window import LoginWindow
from ui.main_window import MainWindow

class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.main_window = None

    def start(self):
        self.login_window.show()
        sys.exit(self.app.exec())

    def open_main_window(self):
        # Закрыть окно авторизации и открыть главное окно
        self.login_window.close()
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app_controller = AppController()
    
    # Связываем авторизацию с открытием главного окна
    app_controller.login_window.open_main_window = app_controller.open_main_window
    app_controller.start()