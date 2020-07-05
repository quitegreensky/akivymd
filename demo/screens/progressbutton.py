from kivy.lang.builder import Builder
from akivymd.uix.progressbutton import AKProgressbutton
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatIconButton
from threading import Thread
import time

Builder.load_string(
    """
#:import MDFillRoundFlatIconButton kivymd.uix.button.MDFillRoundFlatIconButton

<ProgressButton>:
    name: 'ProgressButton'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        FloatLayout:
            AKProgressbutton:
                id: progressbutton_success
                pos_hint: {'center_x': .5, 'center_y':.7}
                button: MDFillRoundFlatIconButton(text='Start', on_release= root.success, icon='language-python')

            AKProgressbutton:
                id: progressbutton_failure
                pos_hint: {'center_x': .5, 'center_y':.3}
                button: MDFillRoundFlatIconButton(text='Start', on_release= root.failure, icon='language-python')
    """)

class ProgressButton(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

    def success(self,*args):
        t= Thread(target=self.start_success)
        t.start()

    def failure(self,*args):
        t= Thread(target=self.start_failure)
        t.start()        

    def start_success(self,*args):
        time.sleep(3)
        return self.ids.progressbutton_success.success()

    def start_failure(self,*args):
        time.sleep(3)
        return self.ids.progressbutton_failure.failure()
