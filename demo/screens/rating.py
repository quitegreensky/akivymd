from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

from akivymd.uix.rating import AKRating

Builder.load_string(
    """
<Rating>:
    name: 'Rating'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]

        FloatLayout:
            AKRating:
                normal_icon: 'star-circle-outline'
                active_icon: 'star-circle'
                pos_hint: {'center_x': .5, 'center_y': .3}
                on_rate: print(self.get_rate())

            AKRating:
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_rate: print(self.get_rate())  
                direction: 'rl'

            AKRating:
                normal_icon: 'star-box-outline'
                active_icon: 'star-box'
                active_color: 1,0,0.4,1
                animation_type: 'grow'    
                pos_hint: {'center_x': .5, 'center_y': .7}
                on_rate: print(self.get_rate())  

    """
)


class Rating(Screen):
    pass
