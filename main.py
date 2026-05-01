import sys
from PyQt6.QtWidgets import QApplication

from gui.view import LPView
from gui.controller import LPController
from logic.game import addition, subtraction, multiplication, division


def main():
    """entry point"""
    app = QApplication([])
    lp_view = LPView()
    lp_view.show()
    LPController(
        view=lp_view,
        add=addition,
        sub=subtraction,
        mult=multiplication,
        div=division
    )
    sys.exit(app.exec())


if __name__ == "__main__":
    main()