from akivymd.uix.bottomnavigation import AKBottomNavigation
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast

Builder.load_string(
'''

<BottomNavigation>
    name: 'BottomNavigation'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        BoxLayout:
            orientation: 'vertical'

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