from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string(
    """
<Navigationrail>:
    name: 'Navigationrail'

    AKNavigationrail:
        id: rail

        AKNavigationrailCustomItem:
            size_hint_y: None
            height: dp(60)
            padding: dp(5)
            MDIconButton:
                icon: 'arrow-left'
                theme_text_color: 'Custom'
                text_color: 1,1,1,1
                on_release:
                    if rail.get_state()=='open': rail.dismiss(); self.icon='menu'
                    else: rail.open(); self.icon='arrow-left'

        AKNavigationrailItem:
            text: 'Withdraw'
            icon: 'wallet-plus'
            on_release: scr_mng.current= 'withdraw'

        AKNavigationrailItem:
            text: 'Deposit'
            icon: 'wallet-plus-outline'
            on_release: scr_mng.current= 'deposit'

        AKNavigationrailItem:
            text: 'Profile'
            icon: 'account-circle-outline'
            on_release: scr_mng.current= 'profile'

        AKNavigationrailCustomItem:

        AKNavigationrailContent:
            ScreenManager:
                id: scr_mng
                Screen:
                    name: 'withdraw'
                    MDLabel:
                        text: 'Withdraw'
                        halign: 'center'

                    MDRectangleFlatButton:
                        text: 'GO BACK'
                        pos_hint: {'center_x': .5, 'center_y': .1}
                        on_release: app.show_screen('Home','back')

                Screen:
                    name: 'deposit'
                    MDLabel:
                        text: 'Deposit'
                        halign: 'center'

                Screen:
                    name: 'profile'
                    MDLabel:
                        text: 'Profile'
                        halign: 'center'
"""
)


class Navigationrail(Screen):
    pass
