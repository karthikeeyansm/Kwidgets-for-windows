from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.core.window import Window
from dark import DarkMode

class WidgetLayout(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DarkMode().isDark():
            self.ids.darkSwitch.active=True
        self.x=0
        self.y=0
  
    def themeswitch(self,instance,value):
        print(value)
        if value:
            DarkMode().toDark()
        else:
            DarkMode().toLight()
    
    def on_touch_move(self, touch):
        print(touch)
        print(Window.top)
        print(Window.left)

        if (touch.spos[0]-self.x)<0:
            Window.left=Window.left-touch.pos[0]
        else:
            Window.left=Window.left+touch.pos[0]
        self.x=touch.pos[0]

        if (touch.spos[1]-self.y)<0:
            Window.top=Window.top-touch.spos[1]
        else:
            Window.top=Window.top+touch.spos[1]
        self.y=touch.pos[1]

        return super().on_touch_move(touch)

    

class WidgetApp(App):
    def build(self):
        # Window.borderless=True
        Window.size=(250,150)
        return WidgetLayout()
    


if __name__=="__main__":
    WidgetApp().run()
