from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class CountdownLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Enter target date (YYYY-MM-DD):", font_size=24)
        self.input = TextInput(multiline=False, font_size=24, size_hint_y=None, height=50)
        self.button = Button(text="Start Countdown", on_press=self.start_countdown, font_size=24, size_hint_y=None, height=50)
        self.result = Label(text="", font_size=24)

        self.add_widget(self.label)
        self.add_widget(self.input)
        self.add_widget(self.button)
        self.add_widget(self.result)

    def start_countdown(self, instance):
        try:
            target_date = datetime.strptime(self.input.text, "%Y-%m-%d")
            now = datetime.now()
            delta = target_date - now
            if delta.days >= 0:
                self.result.text = f"{delta.days} days left!"
            else:
                self.result.text = "That date has already passed."
        except ValueError:
            self.result.text = "Invalid date format. Use YYYY-MM-DD."

class CountdownApp(App):
    def build(self):
        return CountdownLayout()

if __name__ == "__main__":
    CountdownApp().run()
