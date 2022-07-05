from kivy.uix.button import Button


def generate_button(text):
    """
    Create the button with fixed parameters and with the text passed by parameter

    :param text: str
        The text to be displayed on the created button
    :return: Button
        Return button with fixed properties and the specified text as argument
    """
    return Button(
        text=text, font_size=30, background_color="grey",
        pos_hint={"center_x": 0.5, "center_y": 0.5},
    )
