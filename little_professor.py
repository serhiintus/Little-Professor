"""
Little Professor is a game, that generates unsolved expressions and prompts the user for the answer.

This file contains two classes:
LPView to create Little Professor's GUI;
LPController to connect the GUI and the business logic to make the application work.
"""

from functools import partial
import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication,
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


class LPController:
    """Little Professor's controller class."""
    def __init__(self, view, add, sub, mult, div):
        self.view = view
        self.add = add
        self.sub = sub
        self.mult = mult
        self.div = div
        self.connect_signals_and_slots()

    def get_expression_result(self):
        """Get an expression and result."""
        match self.view.operator:
            case "ADDITION":
                self.view.expression, self.view.result = self.add(self.view.level).values()
            case "SUBSTRACTION":
                self.view.expression, self.view.result = self.sub(self.view.level).values()
            case "MULTIPLICATION":
                self.view.expression, self.view.result = self.mult(self.view.level).values()
            case "DIVISION":
                self.view.expression, self.view.result = self.div(self.view.level).values()

    def get_answer(self):
        """Get the answer from a user."""
        answer = self.view.display.text().split("=")[-1].strip()
        return answer

    def delete_answer(self):
        """Delete the answer."""
        if self.view.expression != self.view.get_text():
            return
        self.view.display_expression()

    def start_game(self, operator):
        """Start new game."""
        self.problems = 5
        self.attempts = 3
        self.view.operator = operator
        self.view.correct = 0
        self.view.actualize_status_bar()
        self.get_expression_result()
        self.view.display.setMaxLength(len(self.view.expression) + 10)
        self.view.display_expression()

    def run(self):
        """End the round, check the answer and update atributes."""
        if self.view.expression != self.view.get_text():
            return
        if self.get_answer() == self.view.result:
            self.view.correct += 1
            self.view.actualize_status_bar()
            self.attempts = 3
            self.problems -= 1
            if self.problems > 0:
                self.get_expression_result()
                self.view.display_expression()
            else:
                self.problems = 5
                self.view.display_score()
        elif self.get_answer() != self.view.result:
            self.attempts -= 1
            self.view.display_error()
            if self.attempts > 0:
                QTimer.singleShot(2000, self.view.display_expression)
            else:
                self.attempts = 3
                self.view.display_result()
                self.problems -= 1
                if self.problems > 0:
                    self.get_expression_result()
                    QTimer.singleShot(2000, self.view.display_expression)
                else:
                    self.problems = 5
                    self.view.display_score()

    def level(self):
        """Change the level and update status bar."""
        if self.view.level < 5:
            self.view.level += 1
            self.view.actualize_status_bar()
        else:
            self.view.level = 1
            self.view.actualize_status_bar()

    def build_answer(self, num):
        """Enter the answer in the display."""
        if self.view.expression != self.view.get_text():
            return
        if len(self.get_answer()) > 0 and num == "-":
            return
        answer = self.get_answer() + num
        self.view.display_answer(answer)

    def connect_signals_and_slots(self):
        """Connect all button click signals with the appropriate slots method in the LPController class."""
        numbers = [number for row in self.view.numbers for number in row]
        operations = [operation for row in self.view.operations for operation in row]
        for button_name, button in self.view.button_mapper.items():
            if button_name in numbers[1:]:
                button.clicked.connect(partial(self.build_answer, button_name))
            elif button_name in operations and button_name not in {"LEVEL", "ENTER"}:
                button.clicked.connect(partial(self.start_game, button_name))
        self.view.button_mapper["LEVEL"].clicked.connect(self.level)
        self.view.button_mapper["ENTER"].clicked.connect(self.run)
        self.view.display.returnPressed.connect(self.run)
        self.view.button_mapper["Del"].clicked.connect(self.delete_answer)