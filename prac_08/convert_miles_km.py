"""
CP1404 prac, week 8
convert_miles_km.py
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class DistanceConverterApp(App):

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_input(self):
        try:
            value = float(self.root.ids.miles_input.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        value = self.get_valid_input() + change
        self.root.ids.miles_input.text = str(value)
        self.handle_calculate()


DistanceConverterApp().run()
