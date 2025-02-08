import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox)
from calculator import Calculator

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Calculator")

        self.calculator = Calculator()

        self.num1_label = QLabel("Number 1:")
        self.num1_entry = QLineEdit()
        self.num2_label = QLabel("Number 2:")
        self.num2_entry = QLineEdit()

        self.add_button = QPushButton("+")
        self.subtract_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.divide_button = QPushButton("/")

        self.result_label = QLabel("Result:")
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)


        # Layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.num1_label)
        input_layout.addWidget(self.num1_entry)
        input_layout.addWidget(self.num2_label)
        input_layout.addWidget(self.num2_entry)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.subtract_button)
        button_layout.addWidget(self.multiply_button)
        button_layout.addWidget(self.divide_button)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_display)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(result_layout)

        self.setLayout(main_layout)

        # Connect buttons to functions
        self.add_button.clicked.connect(self.calculate_add)
        self.subtract_button.clicked.connect(self.calculate_subtract)
        self.multiply_button.clicked.connect(self.calculate_multiply)
        self.divide_button.clicked.connect(self.calculate_divide)


    def calculate_add(self):
        self.calculate_operation(self.calculator.add)

    def calculate_subtract(self):
       self.calculate_operation(self.calculator.subtract)

    def calculate_multiply(self):
        self.calculate_operation(self.calculator.multiply)

    def calculate_divide(self):
        self.calculate_operation(self.calculator.divide)

    def calculate_operation(self, operation):
        try:
            num1 = float(self.num1_entry.text())
            num2 = float(self.num2_entry.text())
            result = operation(num1, num2)
            self.result_display.setText(str(result))
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input. Please enter numbers.")
        except ZeroDivisionError as e:
            QMessageBox.critical(self, "Error", str(e))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
