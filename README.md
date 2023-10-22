# LITTLE PROFESSOR
#### Video Demo: <URL https://youtu.be/cz2NqjpCpZs>
#### Description:
This project is an emulator of the Little Professor for PC. Little Professor is a game that works like a backwards calculator, it generates unsolved mathematical expressions and prompts the user for the answer. If the answer is correct, the user's score increases by one. If the answer is incorrect, "EEE" will be displayed. The user has three tries, if all are incorrect, the correct answer is displayed, and the next expression will then appear. The game consists of sets of five mathematical expressions, after completing each set the score is displayed. The game has four mathematical operations: addition, subtraction, multiplication and division. It also has five difficulty levels. The user can pick mathematical operations and difficulty level. If the user change the operation after a set of expressions has already began, the game will restart with a new set of five expressions.

>__Note__: The program requires PyQt6 to be installed, to install it run: `pip install PyQt6`. The Qt libraries in the Linux wheel of the `PyQt6-Qt6` project require OpenSSL v1.1 however some Linux distributions include the incompatible OpenSSL v3. Qt's support for TLS/SSL will not work on Windows when installing wheels with Python v3.7.0 to v3.7.3. This is because of incompatibilities between the different versions of OpenSSL that these versions require.

This project consists of four files:

1. `project.py` is the main file, it contains the main function and functions responsible for business logic. Here are all the functions that are in this file:
   - `main()`\
   Provide the application's entry point. Inside `main()` the program does the following steps:
     * Creates a `QApplication` object named app.
     * Creates a `LPView` object named `lp_view` (application's window).
     * Shows the GUI by calling `.show()` on the `LPView` object.
     * Creates a `LPController` object named `lp_controller`, which connects the GUI to the functions that generates mathematical expression and result, to make the application work.
     * Runs the application's event loop by calling `.exec()`. The call to `.exec()` is wrapped in a call to `sys.exit()`, it allows to cleanly exit Python and release memory resources when the application terminates.
   - `generate_integer(int, divisor: bool = False) -> int`\
    Generate a pseudo random number with the number of digits indicated by the first argument. If divisor is `True`, generate a non-zero number to avoid `ZeroDivisionError` in `division(int)`.
   - `digits(int) -> (int, int)`\
    Calculate the number of digits depending on the level indicated by the argument, and return it for two numbers.
   - `addition(int) -> dict{"expression": str, "result": str}`\
    Takes level as an argument, passes it to `digits(int)` and generate an addition expression and its result.
   - `subtraction(int) -> dict{"expression": str, "result": str}`\
    Takes level as an argument, passes it to `digits(int)` and generate an substraction expression and its result.
   - `multiplication(int) -> dict{"expression": str, "result": str}`\
    Takes level as an argument, passes it to `digits(int)` and generate an multiplication expression and its result.
   - `division(int) -> dict{"expression": str, "result": str}`\
    Takes level as an argument, passes it to `digits(int)` and generate an division expression and its result.

1. `little_professor.py` contains two classes, one to build Little Professor's GUI and the other to connect the GUI to the business logic to make the application work.
   + `LPView` inherits from `QMainWindow` to develop main window–style application. The `QMainWindow` class provides a main application window. A main window provides a framework for building an application's user interface. `QMainWindow` has its own layout which has a center area that can be occupied by any kind of widget. `LPView` class has the following methods:
     - `__init__()`\
        Construct application's GUI with display, status bar, keyboard and fixed main window dimensions.
     - `create_display()`\
        Build a fixed height display with default display text.
     - `create_status_bar()`\
        Build a status bar with default attributes.
     - `create_keyboard()`\
        Build a application's keboard.
     - `display_score()`\
        Show score in the display.
     - `display_expression()`\
        Show expression in the display.
     - `display_error()`\
        Show error in the display.
     - `display_result()`\
        Show correct answer in the display.
     - `display_answer(str)`\
        Show user response in display.
     - `get_text() -> str`\
        Get text from the display.
     - `actualize_status_bar()`\
        Update the status bar's attributes.
   + `LPController` class created to connect the application's GUI with functions responsible for generating mathematical expressions from `project.py` to make the application work. It uses signals and slots - the key features of `PyQt6` to communicate between objects. Every widget of `PyQt6` can emits a signal in response to the specific event, like mouse clicks. A slot is a Python callable. If a signal is connected to a slot then the slot is called when the signal is emitted. `LPController` class has the following methods:
        - `__init__(LPView, addition, subtraction, multiplication, division)`\
        Class initializer, which takes five arguments: instanse of `LPView` (app's GUI), and functions generating mathematical expressions. Then stores these arguments in appropriate instance attributes. Initializer calls `.connect_signals_and_slots()` method to make all the required connections of signals and slots.
        - `get_expression_result()`\
        Get an expression and result.
        - `get_answer() -> str`\
        Get the answer from a user.
        - `delete_answer()`\
        Delete the answer.
        - `start_game(str)`\
        Start a set of five math expressions.
        - `run()`\
        End the round, check the answer and update atributes.
        - `level()`\
        Change the level and update status bar.
        - `build_answer(str)`\
        Enter the answer in the display.
        - `connect_signals_and_slots()`\
        Connect all button click signals with the appropriate slots method in the `LPController` class.

1. `test_project.py` is a file whose purpose is to test functions from `project.py`, which are responsible for business logic, with pytest.
1. `requirements.txt` contains pip-installable libraries that the project requires.