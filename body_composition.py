from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Settings for using Japanese in Kivy(Use Meiryo as a font)
# for Windows settings
resource_add_path('c:/Windows/Fonts')
LabelBase.register(DEFAULT_FONT, 'meiryo.ttc')

# Settings for using Japanese in Matplotlib(Use Meiryo as a font)
# Specify the font path on the local(Windows)
font_location = 'C:/WINDOWS/Fonts/meiryo.ttc'
# Get a font name by specifying its font path(font_location)
font_name = FontProperties(fname=font_location).get_name()
# Change the setting of "font.family" in the configration file(matplotlibrc)
plt.rc('font', family=font_name)

# Initializing Body Composition Data
data = pd.core.frame.DataFrame()


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class SubScreen(Screen):
    graph = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SubScreen, self).__init__(**kwargs)

    def show_graph(self, target):
        # Clear the current graph
        self.graph.clear_widgets()
        if data.empty:
            pass
        else:
            if target == '体重':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [1]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '体脂肪率':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [2]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '体脂肪量':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [9]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '内臓脂肪レベル':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [3]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '骨格筋率':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [5]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '骨格筋量':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [10]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '体年齢':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [7]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == '基礎代謝':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [4]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            elif target == 'BMI':
                fig, ax = plt.subplots()

                data_weight = data.iloc[:, [6]]
                data_weight.plot(ax=ax)

                widget = FigureCanvasKivyAgg(fig)
                self.graph.add_widget(widget)
            else:
                print('Err')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    current_dir = os.path.dirname(os.path.abspath(__file__))


class MainMenu(BoxLayout):
    file_name = ObjectProperty(None)
    info = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self.popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def load(self, path, filename):
        global data
        try:
            self.file_name.text=str(filename[0])
        except Exception as e:
            self.info.text=str(type(e))+' : '+str(e)

        # 体組成のデータの取得
        data = pd.read_csv(filename[0], index_col=0, parse_dates=True, header=0, encoding='UTF8')
        data['体脂肪量(kg)'] = data['体重(kg)'] * data['体脂肪率(%)'] / 100
        data['骨格筋量(kg)'] = data['体重(kg)'] * data['骨格筋率(%)'] / 100

        self.dismiss_popup()

    def dismiss_popup(self):
        self.popup.dismiss()


class BodyCompositionApp(App):
    def __init__(self, **kwargs):
        super(BodyCompositionApp, self).__init__(**kwargs)
        self.title='体組成計データ'

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(SubScreen(name='subscreen'))
        return self.sm


if __name__ == '__main__':
    BodyCompositionApp().run()
