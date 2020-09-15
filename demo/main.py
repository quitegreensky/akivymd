from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem
##
from screens import bottomnavigation,spinners, dataloader, selectionlist, piechart,\
imageviewer, onboarding,progressbutton,silverappbar,badgelayout, addwidget, bottomappbar,\
labelanimation, statusbarcolor, datepicker, progresswidget, hintwidget, windows, navigationrail

from akivymd.uix.statusbarcolor import change_statusbar_color
    
kv='''
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

'''
class DemoApp(MDApp):

    screens=[
        'BottomNavigation','Spinners','Dataloader', 'Selectionlist','Piechart','ImageViewer',
        'Onboarding','ProgressButton','SilverAppbar','BadgeLayout','AddWidgetBehavior', 'BottomAppbar',
        'LabelAnimation', 'StatusbarColor', 'DatePicker', 'ProgressWidget', 'HintWidget','Windows','Navigationrail',
        
    ]
    intro= """here is where you can find all of the widgets. take a look at screens folder to find exmples of how to use them. I will gradually add more and more Awesome widets to this project. Stay tuned!"""

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette= 'Teal'
        self.theme_cls.theme_style='Light'
        self.title='Awesome KivyMD'
        change_statusbar_color(self.theme_cls.primary_color)

    def build(self):
        self.mainkv=Builder.load_string(kv)
        return self.mainkv

    def on_start(self):

        for screen in self.screens:
            self.mainkv.ids.sm.add_widget(eval('Factory.%s()'%screen))

        for list_item in self.screens:
            self.mainkv.ids.menu_list.add_widget(MyMenuItem(
                text=list_item , on_release=self.list_menu_callback
            ))

    def list_menu_callback(self,instance):
        self.show_screen(instance.text) 
        self.mainkv.ids.navdrawer.set_state('close')

    def show_screen(self,name, mode=''):
        if mode=='back':
            self.mainkv.ids.sm.transition.direction='right'
        else:
            self.mainkv.ids.sm.transition.direction='left'
        self.mainkv.ids.sm.current= name 
        return True 


class MyMenuItem(OneLineAvatarListItem):
    pass 

DemoApp().run()