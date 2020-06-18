from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty , ObjectProperty , ListProperty
from kivy.clock import Clock
from kivymd.uix.button import MDIconButton
from kivy.metrics import dp
from kivy.core.window import Window 
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemableBehavior

__all__ = ('AKBottomNavigation')

Builder.load_string( 
"""
<_AKLabel>
    size_hint:None ,None 
    size: dp(48) , dp(48)
    font_style: 'Caption' 
    halign: 'center'
    valign: 'center'
    theme_text_color: 'Custom'
    text_color: root.theme_cls.primary_light

<_AKButton>
    theme_text_color: 'Custom'
    text_color: root.theme_cls.primary_color

<AKBottomNavigation>:
    orientation: 'vertical'
    size_hint_y: None 
    height: self.minimum_height
    BoxLayout:
        size_hint_y: None
        height: dp(14)

        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

    BoxLayout:
        size_hint_y: None
        height: dp(56)

        canvas.before:
            Color:
                rgba: app.theme_cls.bg_dark
            Rectangle:
                pos: self.pos
                size: self.size

        Widget:
            id: _bubble
            bubble_x: 0
            size_hint: None , None 
            size: root.width , dp(70)            
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.bubble_x , dp(28)
                    size: dp(112) , dp(28)
                Ellipse:
                    pos: self.bubble_x+dp(28) , 0
                    size: dp(56) , dp(56)
                Color:
                    rgba: app.theme_cls.bg_dark
                Ellipse:
                    pos: self.bubble_x - dp(28) , 0
                    size: dp(56) , dp(56)
                Ellipse:
                    pos: self.bubble_x + dp(84) , 0
                    size: dp(56) , dp(56)

            FloatLayout:
                id: _text_bar
                size_hint: None , None 
                size: root.width , dp(56)

            FloatLayout:
                id: _buttons_bar
                size_hint: None , None 
                size: root.width , dp(70)
            

"""
)

class _AKLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class _AKButton(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_release(self):
        
        self.index = self.parent.children.index(self)
        AKBottomNavigation.selected = self.index

        for x in self.parent.children: # button 
            x.opacity = 1

        for x in self.parent.parent.children[-1].children: # text 
            x.opacity = 0

        bubble_pos = self.x - dp(31)
        anim_bubble = Animation(bubble_x=bubble_pos , t='out_sine' , duration=0.2)
        anim_text_opacity = Animation(opacity=1 , t='out_sine' , duration=0.2)
        anim_icon_opacity = Animation(opacity=0 , t='out_sine' , duration=0.2)

        anim_icon_opacity.start(self)
        anim_text_opacity.start(self.parent.parent.children[-1].children[self.index])
        anim_bubble.start(self.parent.parent)

    
class AKBottomNavigation(ThemableBehavior,BoxLayout):
    items = ListProperty()
    
    selected = -1
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        Window.bind(on_resize=self._on_resize)
    
    def _clear_bar(self):
        self.ids._buttons_bar.clear_widgets()
        self.ids._text_bar.clear_widgets()
        
    def _update_items(self , items):
        count = len(self.items)
        section_x = 1/(count+1)
        but_pos = section_x
        for x in range(0,count):
            button = _AKButton(
                icon=self.items[x]['icon'],
                pos_hint= {'center_x': but_pos},
                )
            button.bind(on_release = self.items[x]['on_release'])

            label = _AKLabel(
                text=self.items[x]['text'] , 
                pos_hint= {'center_x': but_pos},
                opacity = 0,
            )

            self.ids._text_bar.add_widget(label)
            self.ids._buttons_bar.add_widget(button)
            but_pos += section_x
        self.ids._bubble.bubble_x = Window.size[0]*self.ids._buttons_bar.children[self.selected].pos_hint['center_x']-dp(56)
        self.ids._buttons_bar.children[self.selected].opacity = 0      
        self.ids._text_bar.children[self.selected].opacity = 1

    def _on_resize(self , instance , width , height):
        self.ids._bubble.bubble_x = width*self.ids._buttons_bar.children[self.selected].pos_hint['center_x']-dp(56)
    
    def on_items(self,*args):
        self._clear_bar()
        return self._update_items(self.items)