from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QScrollArea, QCheckBox, QFrame, QFileDialog, QDialog, QTextEdit, QSplitter, QSizePolicy
from PyQt6.QtCore import Qt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Основное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно - Magnelius OSINT")
        self.setFixedSize(1200, 800)

        # Основной макет окна с разделителем для логов
        main_layout = QVBoxLayout()
        splitter = QSplitter(Qt.Orientation.Vertical)

        # Верхняя часть - навигация и карта
        upper_widget = QWidget()
        upper_layout = QHBoxLayout()

        # Панель навигации
        self.nav_panel = self.create_nav_panel()
        upper_layout.addWidget(self.nav_panel)

        # Центральная карта (заглушка)
        self.map_view = QLabel("Карта здесь", alignment=Qt.AlignmentFlag.AlignCenter)
        self.map_view.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        upper_layout.addWidget(self.map_view, stretch=2)

        # Боковая панель управления
        self.side_panel = self.create_side_panel()
        upper_layout.addWidget(self.side_panel)

        upper_widget.setLayout(upper_layout)
        splitter.addWidget(upper_widget)

        # Логи - нижняя панель с возможностью разворачивания
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setFixedHeight(100)  # Высота логов по умолчанию
        self.log_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        splitter.addWidget(self.log_view)

        main_layout.addWidget(splitter)

        # Установка макета в центральное окно
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_nav_panel(self):
        # Панель навигации с кнопками
        nav_panel = QVBoxLayout()

        # Кнопка "Проекты"
        btn_projects = QPushButton("Проекты")
        btn_projects.clicked.connect(self.show_projects)
        nav_panel.addWidget(btn_projects)

        # Кнопка "Экспорт"
        btn_export = QPushButton("Экспорт")
        btn_export.clicked.connect(self.export_data)
        nav_panel.addWidget(btn_export)

        # Кнопка "Экспорт в PDF"
        btn_export_pdf = QPushButton("Экспорт в PDF")
        btn_export_pdf.clicked.connect(self.export_to_pdf)
        nav_panel.addWidget(btn_export_pdf)

        # Кнопка "Отчёты"
        btn_reports = QPushButton("Отчёты")
        btn_reports.clicked.connect(self.generate_report)
        nav_panel.addWidget(btn_reports)

        # Кнопка "Выбор сервисов OSINT"
        btn_osint_services = QPushButton("Выбор сервисов OSINT")
        btn_osint_services.clicked.connect(self.show_osint_services)
        nav_panel.addWidget(btn_osint_services)

        # Объединение в виджет
        nav_widget = QWidget()
        nav_widget.setLayout(nav_panel)
        nav_widget.setFixedWidth(200)

        return nav_widget

    def create_side_panel(self):
        # Боковая панель с элементами управления
        side_panel = QVBoxLayout()

        # Кнопка "Слои"
        btn_layers = QPushButton("Слои")
        btn_layers.clicked.connect(self.show_layers)
        side_panel.addWidget(btn_layers)

        # Кнопка "Фильтры"
        btn_filters = QPushButton("Фильтры")
        btn_filters.clicked.connect(self.show_filters)
        side_panel.addWidget(btn_filters)

        # Кнопка "Настройки"
        btn_settings = QPushButton("Настройки")
        btn_settings.clicked.connect(self.show_settings)
        side_panel.addWidget(btn_settings)

        # Объединение в виджет
        side_widget = QWidget()
        side_widget.setLayout(side_panel)
        side_widget.setFixedWidth(200)

        return side_widget

    # Методы для кнопок панели
    def show_projects(self):
        self.log_message("Открыты проекты.")
        dialog = QDialog(self)
        dialog.setWindowTitle("Проекты")
        dialog.setFixedSize(400, 300)
        label = QLabel("Список проектов", dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog.exec()

    def export_data(self):
        self.log_message("Экспорт данных.")
        file_dialog = QFileDialog.getSaveFileName(self, "Экспорт данных", "", "CSV Files (*.csv);;JSON Files (*.json);;XML Files (*.xml)")
        if file_dialog:
            self.log_message(f"Данные будут экспортированы в файл: {file_dialog[0]}")

    def export_to_pdf(self):
        self.log_message("Экспорт отчёта в PDF.")
        file_dialog = QFileDialog.getSaveFileName(self, "Экспорт отчёта в PDF", "", "PDF Files (*.pdf)")
        if file_dialog[0]:
            pdf_file_path = file_dialog[0]
            self.generate_pdf_report(pdf_file_path)

    def generate_pdf_report(self, file_path):
        c = canvas.Canvas(file_path, pagesize=A4)
        c.drawString(100, 750, "Отчёт по проекту Magnelius OSINT")
        c.drawString(100, 730, "Детали проекта:")
        c.drawString(100, 700, "Данные об объектах, экспортированных с карты")
        c.drawString(100, 680, "Здесь будут данные о фильтрах и слоях")
        c.showPage()
        c.save()
        self.log_message(f"Отчёт успешно экспортирован в {file_path}")

    def generate_report(self):
        self.log_message("Создание отчёта.")
        dialog = QDialog(self)
        dialog.setWindowTitle("Создание отчёта")
        dialog.setFixedSize(400, 300)
        label = QLabel("Генерация отчёта", dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog.exec()

    def show_layers(self):
        self.log_message("Открыто управление слоями.")
        dialog = QDialog(self)
        dialog.setWindowTitle("Управление слоями")
        dialog.setFixedSize(400, 300)
        label = QLabel("Настройка видимости слоёв", dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog.exec()

    def show_filters(self):
        self.log_message("Открыта настройка фильтров.")
        dialog = QDialog(self)
        dialog.setWindowTitle("Настройка фильтров")
        dialog.setFixedSize(400, 300)
        label = QLabel("Фильтрация данных", dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog.exec()

    def show_settings(self):
        self.log_message("Открыты настройки приложения.")
        dialog = QDialog(self)
        dialog.setWindowTitle("Настройки")
        dialog.setFixedSize(400, 300)
        label = QLabel("Настройки приложения", dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog.exec()

    def show_osint_services(self):
        self.osint_window = OSINTServicesWindow(self)
        self.osint_window.show()

    # Метод для добавления сообщений в лог
    def log_message(self, message):
        """Добавление сообщения в текстовый виджет логов"""
        self.log_view.append(message)


# Окно выбора сервисов OSINT
class OSINTServicesWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Выбор сервисов OSINT")
        self.setFixedSize(600, 800)

        self.checkboxes = []  # Инициализация списка чекбоксов
        self.selected_services = []  # Список для сохранения выбранных сервисов

        # Создание основного макета
        layout = QVBoxLayout()

        # Прокручиваемая область для большого списка
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Перечень сервисов по категориям
        self.add_service_section(scroll_layout, "Погода и атмосферные условия", [
            "OpenWeatherMap API", "WeatherAPI", "Windy API", "Meteomatics API"
        ])
        self.add_service_section(scroll_layout, "Качество воздуха", [
            "AirVisual API", "World Air Quality Index API (WAQI)"
        ])
        self.add_service_section(scroll_layout, "Радиация", [
            "Safecast API", "Radiation Data API"
        ])
        self.add_service_section(scroll_layout, "Тепловые аномалии и пожары", [
            "NASA FIRMS", "VIIRS"
        ])
        self.add_service_section(scroll_layout, "Состояние атмосферы", [
            "Copernicus Atmosphere Monitoring Service (CAMS)", "NOAA NCEI"
        ])
        self.add_service_section(scroll_layout, "Спутниковые снимки и мониторинг объектов", [
            "Sentinel Hub", "NASA Worldview API", "Google Earth Engine"
        ])
        self.add_service_section(scroll_layout, "Рельеф местности и картография", [
            "OpenStreetMap (OSM)", "Mapbox API", "USGS National Map"
        ])
        self.add_service_section(scroll_layout, "Энергетическая инфраструктура", [
            "Energinet Open Data API", "Electricity Map"
        ])
        self.add_service_section(scroll_layout, "Ведение боевых действий и военные данные", [
            "Liveuamap API", "FlightRadar24 API", "MarineTraffic API"
        ])
        self.add_service_section(scroll_layout, "Новостные источники", [
            "Telegram API", "NewsAPI", "Twitter API"
        ])

        # Данные по окружающей среде и природе
        self.add_service_section(scroll_layout, "Данные по окружающей среде", [
            "UNEP Environmental Data Explorer", "World Resources Institute (WRI)", "Environmental Data Analysis"
        ])

        # Данные по геолокации и картографии
        self.add_service_section(scroll_layout, "Геолокация и картография", [
            "GeoNames", "MapQuest API", "HERE Maps API", "Google Maps API"
        ])

        # Данные по инфраструктуре
        self.add_service_section(scroll_layout, "Инфраструктура и строительные объекты", [
            "OpenInfraMap", "INFRAPEDIA", "Global Energy Observatory"
        ])

        # Данные по интернет-трафику
        self.add_service_section(scroll_layout, "Интернет и сетевые данные", [
            "Shodan API", "Censys API", "IPinfo API"
        ])

        # Морские и речные данные
        self.add_service_section(scroll_layout, "Морские и речные данные", [
            "NOAA Marine Data", "SeaWeb", "MarineTraffic API", "Global Fishing Watch"
        ])

        # Авиация и космос
        self.add_service_section(scroll_layout, "Авиационные и космические данные", [
            "ADS-B Exchange", "OpenSky Network", "Space-Track", "NORAD"
        ])

        # Данные по безопасности и киберугрозам
        self.add_service_section(scroll_layout, "Данные по безопасности и киберугрозам", [
            "VirusTotal API", "ThreatCrowd API", "GreyNoise"
        ])

        # Установка содержимого прокручиваемой области
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        # Кнопка "Выбрать все"
        select_all_button = QPushButton("Выбрать все сервисы")
        select_all_button.clicked.connect(self.select_all_services)
        layout.addWidget(select_all_button)

        # Кнопка подтверждения выбора
        save_button = QPushButton("Сохранить выбор")
        save_button.clicked.connect(self.save_selection)
        layout.addWidget(save_button)

        # Установка макета в главное окно
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_service_section(self, layout, section_name, services):
        """Добавление секции сервисов"""
        section_label = QLabel(section_name)
        section_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(section_label)

        # Добавление чекбоксов для сервисов
        for service in services:
            checkbox = QCheckBox(service)
            layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)  # Сохраняем чекбоксы для управления выбором

    def select_all_services(self):
        """Выбор всех сервисов (выставить галочки на всех чекбоксах)"""
        for checkbox in self.checkboxes:
            checkbox.setChecked(True)

    def save_selection(self):
        """Сохранение выбранных сервисов и передача их в главное окно"""
        self.selected_services = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        if self.selected_services:
            self.parent().log_message(f"Вы выбрали следующие сервисы: {', '.join(self.selected_services)}")
        else:
            self.parent().log_message("Вы не выбрали ни одного сервиса.")
        self.close()  # Закрыть окно выбора сервисов

    def log_message(self, message):
        """Отправка логов в главное окно"""
        self.parent().log_message(message)