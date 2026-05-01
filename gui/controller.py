from functools import partial
from PyQt6.QtCore import QTimer


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