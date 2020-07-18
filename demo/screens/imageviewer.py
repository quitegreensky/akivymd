from kivy.lang.builder import Builder
from akivymd.uix.imageview import AKImageViewer, AKImageViewerItem
from kivy.uix.screenmanager import Screen

Builder.load_string(
    """
<ImageViewer>:
    name: 'ImageViewer'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: root.name
            left_action_items:[['arrow-left' , lambda x:app.show_screen('Home','back') ]]
    
        FloatLayout:
            MDRaisedButton:
                text:'Open Viewer'
                on_release: root.open()
                pos_hint: {'center_x': .5, 'center_y': .5}    

    """
)    

class ImageViewer(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.viewer= AKImageViewer()
        images= ['assets/google.jpg', 'assets/logo.png', 'assets/fly.jpg']
        for image in images:
            self.viewer.add_widget(AKImageViewerItem(
                source= image
            ))

    def open(self):
        self.viewer.open()
