from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.graphics import Color, Bezier, Line

Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

Builder.load_string("""
<Boxes>:
    labelid: l01
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                FloatLayout:
                    Button:
                        text: "gomba"
                        size_hint: 0.1, 0.1 
                        pos_hint: {"x": 0.8, 'y':0.6}
                        on_press: root.filltable()

                GridLayout: 
                    cols: 9
                    orientation: 'vertical'
                    padding: 0
                    row_default_height: 40
                    col_default_width: 40
                    row_force_default: True
                    col_force_default: True
                    Label:
                        id:00
                        text: "1"
                    Label:
                        id:l01
                        text: "2"
                    Label:
                        id:02
                        text: "3"
                    Label:
                        id:03
                        text: "4"
                    Label:
                        id:04
                        text: "5"
                    Label:
                        id:05
                        text: "6"
                    Label:
                        id:06
                        text: "7"
                    Label:
                        id:07
                        text: "8"
                    Label:
                        id:08
                        text: "9"
                    Label:
                        id:10                    
                        text: "1"
                    Label:
                        id:11
                        text: "2"
                    Label:
                        id:12
                        text: "3"
                    Label:
                        id:13
                        text: "4"
                    Label:
                        id:14
                        text: "5"
                    Label:
                        id:15
                        text: "6"
                    Label:                    
                        id:16
                        text: "7"
                    Label:
                        id:17
                        text: "8"
                    Label:
                        id:18
                        text: "9"
                    Label:
                        id:20
                        text: "1"
                    Label:
                        id:21
                        text: "2"
                    Label:
                        id:22
                        text: "3"
                    Label:
                        id:23
                        text: "4"
                    Label:
                        id:24
                        text: "5"
                    Label:
                        id:25
                        text: "6"
                    Label:
                        id:26
                        text: "7"
                    Label:
                        id:27
                        text: "8"
                    Label:
                        id:28
                        text: "9"
                    Label:
                        id:30
                        text: "1"
                    Label:
                        id:31
                        text: "2"
                    Label:
                        id:32
                        text: "3"
                    Label:
                        id:33
                        text: "4"
                    Label:
                        id:34
                        text: "5"
                    Label:
                        id:35
                        text: "6"
                    Label:
                        id:36
                        text: "7"
                    Label:
                        id:37
                        text: "8"
                    Label:
                        id:38
                        text: "9"
                    Label:
                        id:40
                        text: "1"
                    Label:
                        id:41
                        text: "2"
                    Label:
                        id:42
                        text: "3"
                    Label:
                        id:43
                        text: "4"
                    Label:
                        id:44
                        text: "5"
                    Label:
                        id:45
                        text: "6"
                    Label:
                        id:46
                        text: "7"
                    Label:
                        id:47
                        text: "8"
                    Label:
                        id:48
                        text: "9"
                    Label:
                        id:50
                        text: "1"
                    Label:
                        id:51
                        text: "2"
                    Label:
                        id:52
                        text: "3"
                    Label:
                        id:53
                        text: "4"
                    Label:
                        id:54
                        text: "5"
                    Label:
                        id:55
                        text: "6"
                    Label:
                        id:56
                        text: "7"
                    Label:
                        id:57
                        text: "8"
                    Label:
                        id:58
                        text: "9"
                    Label:
                        id:60
                        text: "1"
                    Label:
                        id:61
                        text: "2"
                    Label:
                        id:62
                        text: "3"
                    Label:
                        id:63
                        text: "4"
                    Label:
                        id:64
                        text: "5"
                    Label:
                        id:65
                        text: "6"
                    Label:
                        id:66
                        text: "7"
                    Label:
                        id:67
                        text: "8"
                    Label:
                        id:68
                        text: "9"
                    Label:
                        id:70
                        text: "1"
                    Label:
                        id:71
                        text: "2"
                    Label:
                        id:72
                        text: "3"
                    Label:
                        id:73
                        text: "4"
                    Label:
                        id:74
                        text: "5"
                    Label:
                        id:75
                        text: "6"
                    Label:
                        id:76
                        text: "7"
                    Label:
                        id:77
                        text: "8"
                    Label:
                        id:78
                        text: "9"
                    Label:
                        id:80
                        text: "1"
                    Label:
                        id:81
                        text: "2"
                    Label:
                        id:82
                        text: "3"
                    Label:
                        id:83
                        text: "4"
                    Label:
                        id:84
                        text: "5"
                    Label:
                        id:85
                        text: "6"
                    Label:
                        id:86
                        text: "7"
                    Label:
                        id:87
                        text: "8"
                    Label:
                        id:88
                        text: "9"

                    
                    
            Screen:
                name: 'screen2'
                Label: 
                    text: 'Another Screen'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Exit'
                on_press: app.stop() 
                """)

class Boxes(FloatLayout):
    def filltable(self):
        self.labelid.text = "6"
class TestApp(App):
    def build(self):
        return Boxes()

if __name__ == '__main__':
    TestApp().run()