from kivy.lang.builder import Builder
from akivymd.uix.piechart import AKPieChart
from kivy.uix.screenmanager import Screen

Builder.load_string(
    """
<Piechart>:
    on_leave: root.remove_chart()
    name: 'Piechart'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
        ScrollView:
            MDBoxLayout:
                adaptive_height: True
                spacing: dp(5)
                padding:dp(5)
                orientation: 'vertical'
                FloatLayout:
                    id: chart_box
                    size_hint_y: None
                    height: dp(400)

        MDBoxLayout:
            adaptive_height: True
            padding: dp(5)
            spacing: dp(4)
            MDRaisedButton:
                text: 'Update'
                on_release: root.update_chart()

    """
)

class Piechart(Screen):
    items= [
        {'Python': 40 , 'Java': 30, 'C++': 10, 'PHP': 8, 'Ruby': 12}
    ] 

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self):
        self.piechart= AKPieChart(
            items= self.items, pos_hint= {'center_x': .5, 'center_y': .5},chart_size= self.width*0.7,
        )
        self.ids.chart_box.add_widget(self.piechart)

    def update_chart(self):
        self.piechart.items= items= [
        {'Python': 70 , 'Dart': 10, 'C#': 10, 'Css': 10}
    ] 

    def remove_chart(self):
        self.ids.chart_box.remove_widget(self.piechart)
