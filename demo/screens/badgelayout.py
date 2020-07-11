from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from akivymd.uix.badgelayout import AKBadgeLayout
Builder.load_string(
'''
<MyAKBadgeLayout@AKBadgeLayout>
    pos_hint: {'center_x': .5, 'center_y': .5}
    badgeitem_padding: dp(5)
    bold: True 

<BadgeLayout>
    name: 'BadgeLayout'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(20)
            
            Widget:

            MyAKBadgeLayout:
                text: '233+'
                offset: 0.5
                MDRaisedButton:
                    text:'Press'

            MyAKBadgeLayout:
                text: '41'
                badgeitem_color: 1,0,0,1
                MDLabel:
                    size_hint: None, None 
                    size: dp(100), dp(20)
                    valign: 'center'
                    halign: 'center'
                    theme_text_color: 'Primary'
                    text:'Press'

            MyAKBadgeLayout:
                text: 'KivyMD'
                offset: 0.5
                position: 'left'
                MDFillRoundFlatButton:
                    text:'Press'                    

            MyAKBadgeLayout:
                text: 'KivyMD'
                offset: 0.5
                position: 'left'
                badgeitem_color: app.theme_cls.primary_color
                MDRoundFlatButton:
                    text:'Press'                    


            MyAKBadgeLayout:
                text: '3'
                position: 'right'
                offset: 0.5
                MDDropDownItem:
                    text:'Press'   

            MyAKBadgeLayout:
                text: ''
                position: 'right'
                badgeitem_color: 1,0,0,1
                MDFloatingActionButton:
                    icon: 'android'   

            Widget:

'''
)

class BadgeLayout(Screen):
    pass 