from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty , ListProperty , BooleanProperty , StringProperty
from kivymd.theming import ThemableBehavior
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp

Builder.load_string("""
<AKSpinnerThreeDots>:
    spacing: self.size[1]
    size_hint: None, None
    size: root.spinner_size*3 , root.spinner_size

    Widget:
        canvas:
            Color:
                rgba: root.theme_cls.primary_color    
            Ellipse:
                size:  root._circle_size1
                pos: [ self.x+self.width/2 - root._circle_size1[0]/2  , self.y+self.height/2 - root._circle_size1[1]/2 ]
    Widget:
        canvas:
            Color:
                rgba: root.theme_cls.primary_color    
            Ellipse:
                size:  root._circle_size2
                pos: [ self.x+self.width/2 - root._circle_size2[0]/2  , self.y+self.height/2 - root._circle_size2[1]/2 ]

    Widget:
        canvas:
            Color:
                rgba: root.theme_cls.primary_color    
            Ellipse:
                size:  root._circle_size3
                pos: [ self.x+self.width/2 - root._circle_size3[0]/2  , self.y+self.height/2 - root._circle_size3[1]/2 ]
""")


class AKSpinnerThreeDots(ThemableBehavior , BoxLayout):

    spinner_size = NumericProperty(48) 
    active = BooleanProperty(False)
    speed = NumericProperty(0.5)
    animation = StringProperty('linear')

    _circle_size1 = ListProperty([0,0])
    _circle_size2 = ListProperty([0,0])
    _circle_size3 = ListProperty([0,0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _start_animate(self , size):
        self.anim1 = Animation(_circle_size1= [size,size],opacity= 1, duration=self.speed ,t=self.animation)\
            + Animation(_circle_size1= [0,0] , duration=self.speed,t=self.animation)\
            + Animation(duration=self.speed)\

        self.anim2 =Animation(_circle_size2= [size,size],opacity= 1, duration=self.speed,t=self.animation)\
            + Animation(_circle_size2= [0,0] , duration=self.speed,t=self.animation)\
            + Animation(duration=self.speed)\

        self.anim3 =Animation(_circle_size3= [size,size],opacity= 1, duration=self.speed,t=self.animation)\
            + Animation(_circle_size3= [0,0] , duration=self.speed,t=self.animation)\
            + Animation(duration=self.speed)\

        self.anim1.repeat = True 
        self.anim2.repeat = True 
        self.anim3.repeat = True 

        self.anim1.start(self)
        Clock.schedule_once(lambda dt: self.anim2.start(self) , self.speed)
        Clock.schedule_once(lambda dt: self.anim3.start(self), self.speed*2)

    def _stop_animate(self):
        self.anim1.cancel_all(self)
        self.anim2.cancel_all(self)
        self.anim3.cancel_all(self)
        self.anim1_stop = Animation(_circle_size1= [0,0] ,opacity= 0, duration=0.1,t=self.animation)
        self.anim2_stop = Animation(_circle_size2= [0,0] ,opacity= 0, duration=0.1,t=self.animation)
        self.anim3_stop = Animation(_circle_size3= [0,0] ,opacity= 0, duration=0.1,t=self.animation)
        self.anim1_stop.start(self)
        self.anim2_stop.start(self)
        self.anim3_stop.start(self)
        
    def on_active(self, *args):
        size= self.size[1]
        if self.active:
            self._start_animate(size)
        else:
            self._stop_animate()