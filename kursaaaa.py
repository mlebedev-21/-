import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QDialog, QPushButton, QLabel, QLineEdit, \
    QTextEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.layout = QVBoxLayout()
        self.central_widget = QLabel()
        self.setCentralWidget(self.central_widget)

        # Установка фоновой картинки на главное окно
        background_img = QPixmap("background.jpg")
        self.central_widget.setPixmap(background_img)

        # Создание главного меню
        self.menu_tab = QTabWidget()

        # Добавление кнопок в главное меню
        self.add_recruit_button = QPushButton("Добавить рекрута")
        self.add_personal_button = QPushButton("Добавить персонал")
        self.show_tables_button = QPushButton("Таблицы")
        self.exit_button = QPushButton("Выход")

        # Добавление кнопок в меню главного окна
        self.layout.addWidget(self.add_recruit_button)
        self.layout.addWidget(self.add_personal_button)
        self.layout.addWidget(self.show_tables_button)
        self.layout.addWidget(self.exit_button)

        self.menu_tab.setLayout(self.layout)
        self.setCentralWidget(self.menu_tab)

        # Подключение функций к кнопкам
        self.add_recruit_button.clicked.connect(self.add_recruit)
        self.add_personal_button.clicked.connect(self.add_personal)
        self.show_tables_button.clicked.connect(self.show_tables)
        self.exit_button.clicked.connect(sys.exit)

        # Выравнивание размера окна под содержимое
        self.adjustSize()

    # Функция добавления рекрута
    def add_recruit(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Добавление рекрута")
        layout = QVBoxLayout(dialog)

        # Добавление полей ввода для данных рекрута
        surname_label = QLabel("Фамилия")
        surname_input = QLineEdit()

        name_label = QLabel("Имя")
        name_input = QLineEdit()

        patronymic_label = QLabel("Отчество")
        patronymic_input = QLineEdit()

        health_group_label = QLabel("Группа здоровья (от А до Г)")
        health_group_input = QLineEdit()

        military_type_label = QLabel("Тип войск")
        military_type_input = QLineEdit()

        city_label = QLabel("Город")
        city_input = QLineEdit()

        birthdate_label = QLabel("Дата рождения")
        birthdate_input = QLineEdit()

        # Добавление кнопок
        back_button = QPushButton("Назад")
        add_button = QPushButton("Добавить")

        # Добавление элементов в окно добавления рекрута
        layout.addWidget(surname_label)
        layout.addWidget(surname_input)
        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(patronymic_label)
        layout.addWidget(patronymic_input)
        layout.addWidget(health_group_label)
        layout.addWidget(health_group_input)
        layout.addWidget(military_type_label)
        layout.addWidget(military_type_input)
        layout.addWidget(city_label)
        layout.addWidget(city_input)
        layout.addWidget(birthdate_label)
        layout.addWidget(birthdate_input)
        layout.addWidget(add_button)
        layout.addWidget(back_button)

        def add_recruit_to_table():
            # Получение данных из полей ввода
            surname = surname_input.text()
            name = name_input.text()
            patronymic = patronymic_input.text()
            health_group = health_group_input.text()
            military_type = military_type_input.text()
            city = city_input.text()
            birthdate = birthdate_input.text()

            # Добавление данных в таблицу
            recruit_data = {"Фамилия": [surname], "Имя": [name], "Отчество": [patronymic],
                            "Группа здоровья": [health_group], "Тип войск": [military_type], "Город": [city],
                            "Дата рождения": [birthdate]}
            df = pd.DataFrame(recruit_data)
            df.to_excel("recruits.xlsx", index=False)

            # Очистка полей ввода
            surname_input.setText("")
            name_input.setText("")
            patronymic_input.setText("")
            health_group_input.setText("")
            military_type_input.setText("")
            city_input.setText("")
            birthdate_input.setText("")

        add_button.clicked.connect(add_recruit_to_table)
        back_button.clicked.connect(dialog.reject)

        # Выравнивание размера окна под содержимое
        dialog.adjustSize()

        dialog.exec()

    # Функция добавления персонала
    def add_personal(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Добавление персонала")
        layout = QVBoxLayout(dialog)

        # Добавление полей ввода для данных персонала
        surname_label = QLabel("Фамилия")
        surname_input = QLineEdit()

        name_label = QLabel("Имя")
        name_input = QLineEdit()

        patronymic_label = QLabel("Отчество")
        patronymic_input = QLineEdit()

        work_experience_label = QLabel("Количество проработанных лет")
        work_experience_input = QLineEdit()

        position_label = QLabel("Должность")
        position_input = QLineEdit()

        city_label = QLabel("Город")
        city_input = QLineEdit()

        birthdate_label = QLabel("Дата рождения")
        birthdate_input = QLineEdit()

        # Добавление кнопок
        back_button = QPushButton("Назад")
        add_button = QPushButton("Добавить")

        # Добавление элементов в окно добавления персонала
        layout.addWidget(surname_label)
        layout.addWidget(surname_input)
        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(patronymic_label)
        layout.addWidget(patronymic_input)
        layout.addWidget(work_experience_label)
        layout.addWidget(work_experience_input)
        layout.addWidget(position_label)
        layout.addWidget(position_input)
        layout.addWidget(city_label)
        layout.addWidget(city_input)
        layout.addWidget(birthdate_label)
        layout.addWidget(birthdate_input)
        layout.addWidget(add_button)
        layout.addWidget(back_button)

        def add_personal_to_table():
            # Получение данных из полей ввода
            surname = surname_input.text()
            name = name_input.text()
            patronymic = patronymic_input.text()
            work_experience = work_experience_input.text()
            position = position_input.text()
            city = city_input.text()
            birthdate = birthdate_input.text()

            # Добавление данных в таблицу
            personal_data = {"Фамилия": [surname], "Имя": [name], "Отчество": [patronymic],
                             "Количество проработанных лет": [work_experience], "Должность": [position],
                             "Город": [city], "Дата рождения": [birthdate]}
            df = pd.DataFrame(personal_data)
            df.to_excel("personal.xlsx", index=False)

            # Очистка полей ввода
            surname_input.setText("")
            name_input.setText("")
            patronymic_input.setText("")
            work_experience_input.setText("")
            position_input.setText("")
            city_input.setText("")
            birthdate_input.setText("")

        add_button.clicked.connect(add_personal_to_table)
        back_button.clicked.connect(dialog.reject)

        # Выравнивание размера окна под содержимое
        dialog.adjustSize()

        dialog.exec()

    # Создание таблиц
    def show_tables(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Таблицы")
        layout = QVBoxLayout(dialog)

        # Создание виджетов таблиц
        table_widget = QTableWidget()
        recruit_table_button = QPushButton("Таблица рекрутов")
        personal_table_button = QPushButton("Таблица персонала")
        back_button = QPushButton("Назад")

        def open_recruit_table():
            try:
                # Открытие таблицы с рекрутами
                df = pd.read_excel("recruits.xlsx")
                table_widget.setColumnCount(df.shape[1])
                table_widget.setRowCount(df.shape[0])
                table_widget.setHorizontalHeaderLabels(df.columns)

                for i in range(df.shape[0]):
                    for j in range(df.shape[1]):
                        item = QTableWidgetItem(str(df.iloc[i, j]))
                        table_widget.setItem(i, j, item)
            except Exception as e:
                print(e)

        def open_personal_table():
            try:
                # Открытие таблицы с персоналом
                df = pd.read_excel("personal.xlsx")
                table_widget.setColumnCount(df.shape[1])
                table_widget.setRowCount(df.shape[0])
                table_widget.setHorizontalHeaderLabels(df.columns)

                for i in range(df.shape[0]):
                    for j in range(df.shape[1]):
                        item = QTableWidgetItem(str(df.iloc[i, j]))
                        table_widget.setItem(i, j, item)
            except Exception as e:
                print(e)

        recruit_table_button.clicked.connect(open_recruit_table)
        personal_table_button.clicked.connect(open_personal_table)
        back_button.clicked.connect(dialog.reject)

        # Добавление элементов в окно таблиц
        layout.addWidget(table_widget)
        layout.addWidget(recruit_table_button)
        layout.addWidget(personal_table_button)
        layout.addWidget(back_button)

        # Выравнивание размера окна под содержимое
        dialog.adjustSize()

        dialog.exec()


# Создание главного окна приложения
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())