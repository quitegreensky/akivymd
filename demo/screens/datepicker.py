from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

from akivymd.uix.datepicker import AKDatePicker

Builder.load_string(
    """
<DatePicker>:
    name: 'DatePicker'
    on_leave: date.text= ''

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back')]]

        FloatLayout:
            MDRaisedButton:
                text: 'Open'
                on_release: root.open()
                pos_hint: {'center_x': .5, 'center_y': .5}

            MDLabel:
                id: date
                text: ''
                halign: 'center'
                valign: 'center'
                size_hint_y: 0.2
                pos_hint: {'center_x': .5, 'center_y': .3}

"""
)


class DatePicker(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.date = AKDatePicker(callback=self.callback)

    def callback(self, date):
        if not date:
            return

        self.ids.date.text = "%d / %d / %d" % (date.day, date.month, date.year)

    def open(self):
        self.date.open()
