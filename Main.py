from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.last_was_equal = False
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=32
        )

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.solution.text = ""
        elif text in self.operators:
            if self.solution.text and not self.last_was_operator:
                self.solution.text += text
                self.last_was_operator = True
        else:
            if self.last_was_equal:
                self.solution.text = ""
            self.solution.text += text
            self.last_was_operator = False
            self.last_was_equal = False

    def on_solution(self, instance):
        try:
            self.solution.text = str(eval(self.solution.text))
            self.last_was_equal = True
        except Exception:
            self.solution.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
