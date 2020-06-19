from akivymd.uix.selectionlist import AKSelectList,AKSelectListAvatarItem
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
Builder.load_string(
    """
<Selectionlist>:
    name: 'Selectionlist'
    on_leave: 
        # root.stop_animation()

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        
        ScrollView:
            AKSelectList:
                id: selectionlist

        MDBoxLayout:
            adaptive_height: True
            padding: dp(5)
            spacing: dp(5)
            MDRaisedButton:
                text: 'Ok'
                on_release: root.get_selected()
            MDRaisedButton:
                text: 'Clear'
                on_release: root.clear_selected()
            MDRaisedButton:
                text: 'Select All'
                on_release: root.select_all()                
    """
)

class Selectionlist(Screen):

    def on_enter(self):

        self.ids.selectionlist.clear_widgets()
        for x in range(20):
            self.ids.selectionlist.add_widget(AKSelectListAvatarItem(
                first_label= 'Item %d'%x,
                second_label= 'Description for item %d'%x,
                source= 'assets\logo.png'
            ))

    def on_leave(self):
        return self.clear_selected()

    def get_selected(self):
        items= self.ids.selectionlist.get_selection()  
        text= ''
        for x in items :
            text+= ', %s'%x
        return toast(text)

    def clear_selected(self):
        return self.ids.selectionlist.clear_selection()

    def select_all(self):
        return self.ids.selectionlist.select_all()