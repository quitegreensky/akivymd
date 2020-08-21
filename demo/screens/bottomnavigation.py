from akivymd.uix.bottomnavigation import AKBottomNavigation
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from akivymd.uix.bottomnavigation2 import AKBottomNavigation2

Builder.load_string(
'''

<BottomNavigation>
    name: 'BottomNavigation'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(40)
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        BoxLayout:
            orientation: 'vertical'

        AKBottomNavigation2:
            bg_color: app.theme_cls.bg_dark

            Button_Item:
                text: 'Alert'
                icon: 'bell-outline'
                icon_color: 0.3,0.2,0.3 ,1
                text_color: 0.3,0.2,0.3 ,1
                button_bg_color: 0.7,0.5,0.7,1
                badge_text: '+12'

            Button_Item:
                text: 'Bank'
                badge_text: ''
                icon: 'bank-outline'
                icon_color: 0.2,0.2,0.6 ,1
                text_color: 0.2,0.2,0.6 ,1
                button_bg_color: 0.6,0.6,1,1

            Button_Item:
                text: 'Download'
                icon: 'arrow-down-bold-outline'
                icon_color: 0.8,0,0 ,1
                text_color: 0.8,0,0 ,1
                button_bg_color: 1,0.6,0.6 ,1    
                badge_disabled: True 

            Button_Item:
                text: 'Account'
                icon: 'account-circle-outline'
                icon_color: 0,0.4,0 ,1
                text_color: 0,0.4,0 ,1
                button_bg_color: 0.4,1,0.4 ,1 
                badge_text: '+2'  

        AKBottomNavigation:
            items: root.bottomnavigation_items
'''
)

class BottomNavigation(Screen):

    bottomnavigation_items=[
        {'icon':'android' , 'text': 'android' , 'on_release': lambda x: toast('android')},
        {'icon':'menu' , 'text': 'menu' , 'on_release': lambda x: toast('menu')},
        {'icon':'account' , 'text': 'account' , 'on_release': lambda x: toast('account')},

    ]