"""
CP1404 prac, week 8
dynamic_labels.py
Estimate: 40min
Actual: 1 hour
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Adrianne', 'Belethor', 'Dorthe', 'Hod', 'Tiber']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.create_labels(temp_label)


DynamicLabelsApp().run()
