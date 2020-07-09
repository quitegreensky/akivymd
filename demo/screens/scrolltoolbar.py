from akivymd.uix.scrolltoolbar import AKScrollToolbar,AKScrollViewHeader,AKSrollToolbarContent
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

Builder.load_string(
    """
<ScrollToolbar>:
    name: 'ScrollToolbar'

    AKScrollToolbar:
        max_height: dp(300)
        title: root.name
        left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        pin_top: True
        hide_toolbar: True  
        radius: dp(20)
        toolbar_bg: app.theme_cls.primary_color
        
        AKScrollViewHeader:     
            orientation: 'vertical'     
            Image:
                source: 'assets/fly.jpg'
                allow_stretch: True 
                keep_ratio: False

        AKSrollToolbarContent:
            padding: dp(10)
            id: content
            size_hint_y: None 
            height: self.minimum_height
            orientation: 'vertical'
            md_bg_color: app.theme_cls.primary_color

"""
)

class ScrollToolbar(Screen):

    def on_enter(self, *args):
        
        for x in range(30):
            self.ids.content.add_widget(OneLineListItem(text='Item %d'%x))

    def on_leave(self, *args):
        self.ids.content.clear_widgets()