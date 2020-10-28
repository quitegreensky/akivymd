from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

from akivymd.uix.progresswidget import AKCircularProgress

Builder.load_string(
    """
<ProgressWidget>:
    name: 'ProgressWidget'
    on_leave:
        progress_relative= 0
        progress_percent= 0

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]

        BoxLayout:
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(30)
            AKCircularProgress:
                id: progress_percent
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint: None, None
                size: dp(100), dp(100)
                percent_type: 'percent'
                start_deg: 180
                end_deg: 540

            BoxLayout:
                spacing: dp(5)
                BoxLayout:
                MDRaisedButton:
                    text: '0'
                    on_release: progress_percent.current_percent= 0

                MDRaisedButton:
                    text: '45'
                    on_release: progress_percent.current_percent= 45

                MDRaisedButton:
                    text: '100'
                    on_release: progress_percent.current_percent= 100
                BoxLayout:

            AKCircularProgress:
                id: progress_relative
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint: None, None
                size: dp(100), dp(100)
                percent_type: 'percent'
                start_deg: 240
                end_deg: 480
                percent_type: 'relative'
                max_percent: 25

            BoxLayout:
                spacing: dp(5)
                BoxLayout:
                MDRaisedButton:
                    text: '0'
                    on_release: progress_relative.current_percent= 0

                MDRaisedButton:
                    text: '10'
                    on_release: progress_relative.current_percent= 10

                MDRaisedButton:
                    text: '25'
                    on_release: progress_relative.current_percent= 25
                BoxLayout:

    """
)


class ProgressWidget(Screen):
    pass
