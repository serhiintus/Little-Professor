from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLineEdit,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
)


WINDOW_WIDTH = 260
WINDOW_HEIGHT = 300
DISPLAY_HEIGHT = 60
ERROR_MSG = "EEE"


class LPView(QMainWindow):
    """Little Professor's main window (GUI or view)."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Little Professor")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.main_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.level = 1
        self.operator = "addition"
        self.correct = 0
        self.expression = ""
        self.result = "0"
        self.create_display()
        self.create_status_bar()
        self.create_keyboard()

    def create_display(self):
        self.display = QLineEdit("Select a math operation to start the game.")
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setReadOnly(True)
        self.main_layout.addWidget(self.display)

    def create_status_bar(self):
        self.status_bar = QLabel(
            f"level: {self.level}   operation: {self.operator.lower()}   score: {self.correct}"
        )
        self.main_layout.addWidget(self.status_bar)

    def create_keyboard(self):
        self.numbers = [
            ["Del", "7", "8", "9"],
            ["-", "4", "5", "6"],
            ["0", "1", "2", "3"],
        ]
        self.operations = [
            ["ADDITION", "SUBSTRACTION"],
            ["MULTIPLICATION", "DIVISION"],
            ["LEVEL", "ENTER"],
        ]
        self.button_mapper = {}
        self.keyboard_layout = QGridLayout()

        for row, buttons in enumerate(self.numbers):
            for col, button in enumerate(buttons):
                self.button_mapper[button] = QPushButton(button)
                self.keyboard_layout.addWidget(self.button_mapper[button], row, col)

        for row, buttons in enumerate(self.operations, 3):
            for col, button in enumerate(buttons):
                self.button_mapper[button] = QPushButton(button)
                if col == 1:
                    self.keyboard_layout.addWidget(
                        self.button_mapper[button], row, col + 1, 1, 2
                    )
                self.keyboard_layout.addWidget(
                    self.button_mapper[button], row, col, 1, 2
                )

        self.main_layout.addLayout(self.keyboard_layout)

    def display_score(self):
        """Show score in the display."""
        self.display.setMaxLength(20)
        self.display.setText(f"You score {self.correct} points")

    def display_expression(self):
        """Show expression in the display."""
        self.display.setText(self.expression + " = ")

    def display_error(self):
        """Show error in the display."""
        self.display.setText(ERROR_MSG)

    def display_result(self):
        """Show correct answer in the display."""
        self.display.setText(self.expression + " = " + self.result)

    def display_answer(self, text):
        """Show user response in display."""
        self.display.setText(self.expression + " = " + text)

    def get_text(self):
        """Get text from the display."""
        return self.display.text().split("=")[0].strip()

    def actualize_status_bar(self):
        """Update the status bar's attributes."""
        self.status_bar.setText(
            f"level: {self.level}   operation: {self.operator.lower()}   score: {self.correct}"
        )