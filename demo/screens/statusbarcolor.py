from kivy.lang.builder import Builder
from akivymd.uix.statusbarcolor import change_statusbar_color
from kivy.uix.screenmanager import Screen

Builder.load_string(
    """
<StatusbarColor>:
    name: 'StatusbarColor'
    on_leave: root.change_color( app.theme_cls.primary_color )
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]

        FloatLayout:
            MDRaisedButton:
                text: 'Red'
                on_release: root.change_color( (1,0,0,1) )
                pos_hint: {'center_x': .5, 'center_y': 0.1}

            MDRaisedButton:
                text: 'Green'
                on_release: root.change_color( (0,0.7,0,1) )
                pos_hint: {'center_x': .5, 'center_y': 0.3}    

            MDRaisedButton:
                text: 'Blue'
                on_release: root.change_color( (0,0,1,1) )
                pos_hint: {'center_x': .5, 'center_y': 0.5}
            
            MDRaisedButton:
                text: 'Yellow'
                on_release: root.change_color( (1,1,0,1) )
                pos_hint: {'center_x': .5, 'center_y': 0.7}

            MDRaisedButton:
                text: 'White'
                on_release: root.change_color( (1,1,1,1) )
                pos_hint: {'center_x': .5, 'center_y': 0.9}                                              
    """
)

class StatusbarColor(Screen):

    def change_color(self, color):
        return change_statusbar_color(color)