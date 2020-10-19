from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string(
    """
<WidgetHint@AKHintWidgetItem>
    orientation: 'vertical'
    mode_text: ''
    pos_text: ''
    canvas.before:
        Color:
            rgba: app.theme_cls.bg_normal
        RoundedRectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        halign: 'center'
        valign: 'center'
        font_size: dp(12)
        text: 'Custom Widget'
    MDLabel:
        halign: 'center'
        valign: 'center'
        font_size: dp(12)
        text: 'mode= '+ root.mode_text
    MDLabel:
        halign: 'center'
        valign: 'center'
        font_size: dp(12)
        text: 'pos= '+root.pos_text

<HintWidget>:
    name: 'HintWidget'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back')]]

        FloatLayout:

            AKHintWidget:
                size_hint: None, None
                size: dp(400), dp(400)
                pos_hint: {'x': .05, 'center_y': .5}
                show_mode: 'hover'
                hintwidget_pos: 'tr'

                canvas.before:
                    Color:
                        rgba: 1,1,1,1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        source: 'assets/fly.jpg'

                WidgetHint:
                    mode_text: 'hover'
                    pos_text: 'top right'

            AKHintWidget:
                size_hint: None, None
                size: dp(400), dp(400)
                pos_hint: {'right': .95, 'center_y': .5}
                show_mode: 'touch'
                hintwidget_pos: 'bl'
                auto_dismiss: False
                open_button: 'right'
                canvas.before:
                    Color:
                        rgba: 1,1,1,1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        source: 'assets/fly.jpg'

                WidgetHint:
                    mode_text: 'touch right button'
                    pos_text: 'bottom left'
                    MDRaisedButton:
                        text: 'Button'
                        pos_hint: {'center_x': .5}

"""
)


class HintWidget(Screen):
    pass
