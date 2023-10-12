


class RadioButtonBehaviour():

    def __init__(self):
        self.button_list = []

    def append(self, button):
        self.button_list.append(button)
        button.config(command=self.radio_button_command(button))

    def radio_button_command(self, current_button):
        def command():
            if current_button["relief"] == "sunken":
                current_button.config(state="normal", relief="raised")
            else:
                for button in self.button_list:
                    if button["relief"] == "sunken":
                        button.config(state="normal", relief="raised")
                current_button.config(state="active", relief="sunken")
        return command
