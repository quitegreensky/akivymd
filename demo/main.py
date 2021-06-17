from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.toast import toast
from kivy.core.clipboard import Clipboard
import webbrowser
from kivymd_extensions.akivymd.uix.spinners import *
from pygments.styles.fruity import FruityStyle
from pygments.styles.solarized import SolarizedDarkStyle

kv = '''
<AKSpinnerDemo@Screen>
#: import get_color_from_hex kivy.utils.get_color_from_hex
#:import toast kivymd.toast.toast
<Star@MDIconButton>:
    icon: "star-outline"
    on_release: 
        self.icon = "star" #if self.icon == "star-outline" else self.icon = "star"

ScreenManager:
    AKSpinnerDemo:

<AKSpinnerDemo>:
    name: "akSpinner"
    MDBoxLayout:
        orientation:'vertical'
        id: ver_layout
        MDToolbar:
            md_bg_color: get_color_from_hex('#1520A6')
            title: "Spinner-AKivymd"
            id: top_bar
            left_action_items:[['chevron-left', lambda x: x]]
            right_action_items: [["view-list", lambda x: x], ["white-balance-sunny", lambda x:app.dark_theme(code, output_card)], ["arrow-right", lambda x:x]]

        MDBoxLayout:
            orientation:'horizontal'
            adaptive_height: True
            MDRaisedButton:
                id: outputButton
                text: "Output"
                size_hint_x:0.5
                elevation:15
                md_bg_color: top_bar.md_bg_color
                on_release:
                    app.hide_code(self, top_bar)
                    self.md_bg_color = top_bar.md_bg_color
                    codeButton.md_bg_color = 0, .1, 0.5, .5
            MDRaisedButton:
                id: codeButton
                text: "Code"
                size_hint_x:0.5
                elevation: 15
                on_release: 
                    app.show_code(self, top_bar)
                    self.md_bg_color = top_bar.md_bg_color
                    outputButton.md_bg_color = 0, .1, 0.5, .5
        MDCard:
            id: output_card
            orientation:'vertical'
            spacing: "50dp"
            elevation: 20
            padding: "20dp"
            MDLabel:
                text: "[b]AKivymd spinner classes:[/b]"
                font_style: "H5"
                markup:True
                halign: "center"
            SpinnerThreeDots:
                active: True
                pos_hint:{"center_x":0.5}
            MDLabel:
                text: "AKSpinnerThreeDots"
                halign:"center"
            FoldingCube:
                active: True
                pos_hint:{"center_x":0.5}
            MDLabel:
                text: "AKSpinnerFoldingCube"
                halign:"center"
            CircleFlip:
                active:True
                pos_hint:{"center_x":0.5}
            MDLabel:
                text: "AKSpinnerCircleFlip"
                halign:"center"
            DoubleBounce:
                active:True
                pos_hint:{"center_x":0.5}
            MDLabel:
                text: "AKSpinnerDoubleBounce"
                halign:"center"
    CodeInput:
        id: code
        size_hint: 0, 0.88
        readonly: True   
        selection:False     
        background_color: 1,1,1,1
    MDFloatingActionButtonSpeedDial:
        data: app.data
        callback: app.speed_dial
        bg_color_stack_button: top_bar.md_bg_color
        bg_color_root_button: self.bg_color_stack_button
        root_button_anim: True
'''


class SpinnerThreeDots(AKSpinnerThreeDots): pass
class CircleFlip(AKSpinnerCircleFlip): pass
class DoubleBounce(AKSpinnerDoubleBounce): pass
class FoldingCube(AKSpinnerFoldingCube): pass

class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.codeStyle = FruityStyle
        self.data = {
            "github repo": "github",
            "copy code": "content-copy"
        }
        self.akSpinner = open("implementation.py", "r").read()

    def build(self):
        return Builder.load_string(kv)

    def hide_code(self, caller, top_bar):
        hide_anim = Animation(size_hint_x=(0), duration=0.2)
        hide_anim.start(self.root.get_screen('akSpinner').ids.code)
        self.root.get_screen('akSpinner').ids.code.text = ''

    def show_code(self, caller, top_bar):
        obj = self.root.get_screen('akSpinner').ids.code
        anim = Animation(size_hint_x=(1), duration=0.2)
        anim.start(obj)
        obj.text = self.akSpinner

    # self.root.get_screen('akSpinner').remove_widget(self.sdBtn_obj)

    def speed_dial(self, instance):
        if instance.icon == 'content-copy':
            Clipboard.copy("")
            toast("copied!")
        else:
            webbrowser.open_new('https://github.com/quitegreensky/akivymd/blob/master/akivymd/uix/spinners.py')

    def dark_theme(self, code_input_obj, output_card_obj):
        codeInput = self.root.get_screen("akSpinner").ids.code
        if codeInput.background_color == [1, 1, 1, 1]:
            drkAnim = Animation(md_bg_color=[0, 0, 0, 1], duration=.3)
            drkAnim.start(output_card_obj)
            code_drkAnim = Animation(background_color=[.5, .5, .5, 1], duration=.3)
            code_drkAnim.start(code_input_obj)
            self.theme_cls.theme_style = "Dark"
            return
        else:
            lightAnim = Animation(md_bg_color=[1, 1, 1, 1])
            lightAnim.start(output_card_obj)
            code_lightAnim = Animation(background_color=[1, 1, 1, 1], duration=.3)
            code_lightAnim.start(code_input_obj)
            self.theme_cls.theme_style = "Light"
            return


if __name__ == "__main__":
    DemoApp().run()
