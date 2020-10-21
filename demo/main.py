import re
import akivymd
"""
this line makes all the screens automatically register factory
Use this line to all your projects (main.py)
"""
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp

from akivymd.uix.statusbarcolor import change_statusbar_color
from screens import (
    addwidget,
    badgelayout,
    bottomappbar,
    bottomnavigation,
    dataloader,
    datepicker,
    dialogs,
    hintwidget,
    imageviewer,
    labelanimation,
    navigationrail,
    onboarding,
    piechart,
    progressbutton,
    progresswidget,
    selectionlist,
    silverappbar,
    spinners,
    statusbarcolor,
    windows,
)

kv = """
<MyMenuItem@OneLineAvatarListItem>
    IconLeftWidget:
        icon: 'language-python'

Screen:
    ScreenManager:
        id: sm
        Screen:
            name: 'Home'
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: app.title
                    left_action_items:[['menu' , lambda x: navdrawer.set_state("open") ]]
                BoxLayout:
                    padding:dp(20)
                    MDLabel:
                        text: app.intro
                        theme_text_color: 'Primary'
                        halign: 'center'

    MDNavigationDrawer:
        id: navdrawer
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                Image:
                    source:'assets/logo.png'
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint: None,None
                    size: dp(200), dp(200)
                MDList:
                    id: menu_list

"""


class DemoApp(MDApp):

    screens = {
        "BottomNavigation": "Bottom Navigation",
        "Spinners": "Spinners",
        "Dataloader": "Dataloader",
        "Selectionlist": "Selectionlist",
        "Piechart": "Piechart",
        "ImageViewer": "Image Viewer",
        "Onboarding": "Onboarding",
        "ProgressButton": "Progress Button",
        "SilverAppbar": "Silver Appbar",
        "BadgeLayout": "Badge Layout",
        "AddWidgetBehavior": "AddWidget Behavior",
        "BottomAppbar": "Bottom Appbar",
        "LabelAnimation": "Label Animation",
        "StatusbarColor": "Statusbar Color",
        "DatePicker": "Date Picker",
        "ProgressWidget": "Progress Widget",
        "HintWidget": "Hint Widget",
        "Windows": "Windows",
        "Navigationrail": "Navigationrail",
        "Dialogs": "Dialogs",
    }
    intro = """Here is where you can find all of the widgets. Take a look at screens folder to find examples of how to use them. We will gradually add more and more Awesome widgets to this project. Stay tuned!"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.title = "Awesome KivyMD"
        change_statusbar_color(self.theme_cls.primary_color)

    def build(self):
        self.mainkv = Builder.load_string(kv)
        return self.mainkv

    def on_start(self):

        for screen in self.screens.keys():
            self.mainkv.ids.sm.add_widget(eval("Factory.%s()" % screen))

        for list_item in self.screens.values():
            self.mainkv.ids.menu_list.add_widget(
                Factory.MyMenuItem(
                    text=list_item, on_release=self.list_menu_callback
                )
            )

    def list_menu_callback(self, instance):
        screen_name = re.sub(" ", "", instance.text)
        self.show_screen(screen_name)
        self.mainkv.ids.navdrawer.set_state("close")

    def show_screen(self, name, mode=""):
        if mode == "back":
            self.mainkv.ids.sm.transition.direction = "right"
        else:
            self.mainkv.ids.sm.transition.direction = "left"
        self.mainkv.ids.sm.current = name
        return True


DemoApp().run()
