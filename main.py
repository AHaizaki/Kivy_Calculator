import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from button_generator.button_generator import generate_button


class MainApp(App):
    """
    Class representing the application

    Attributes
    ----------
    operators: list[str]
        List of the different operators used by the calculator

    last_was_operator: bool
        Check if the last button pressed is an operator.

    last_button: str
        Value of the last button clicked

    solution: TextInput
        Input containing all the operations written by the user.

    Methods
    -------
    on_button_press(instance=Button)
        After selecting a button except for the solution button,
        it will call this function to perform its respective functionality.

    check_button_text(button_text=str, current_input_text=str)
        Check the selected button and perform its functionality.

    on_solution(instance=Button)
        Performs the calculations written in the input
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.solution = TextInput(background_color="black", foreground_color="white",
                                  multiline=False, halign="right", font_size=45, readonly=True)

    def build(self):
        self.icon = "assets/images/icon.jpg"
        self.title = "Calculator"
        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = generate_button(label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = generate_button("=")
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        """
        After selecting a button except for the solution button,
        it will call this function to perform its respective functionality.

        :param instance: Button
            The button that has been pressed
        """
        current_input_text = self.solution.text
        button_text = instance.text

        self.check_button_text(button_text, current_input_text)

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def check_button_text(self, button_text, current_input_text):
        """
        Check the selected button and perform its functionality.

        :param button_text: str
            Value of the selected button
        :param current_input_text:
            Text written in the input
        """

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current_input_text and (
                    self.last_was_operator and button_text in self.operators
            ):
                return
            elif (current_input_text == "" or current_input_text == "error") and button_text in self.operators:
                return
            elif current_input_text == "error":
                self.solution.text = button_text
            else:
                new_text = current_input_text + button_text
                self.solution.text = new_text

    def on_solution(self, instance):
        """
        Performs the calculations written in the input

        :param instance: Button
            The button that has been pressed
        """

        text = self.solution.text
        try:
            if text:
                solution = str(eval(re.sub(r'\b0+(?!\b)', '', self.solution.text)))
                self.solution.text = solution
        except ZeroDivisionError:
            self.solution.text = "error"


if __name__ == "__main__":
    app = MainApp()
    app.run()
